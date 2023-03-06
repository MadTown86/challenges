import random

import numpy
from typing import Self
from time import perf_counter
from collections import defaultdict
import statistics

OPEN = 0
MARKED = 1
MOVES = 2
CURRENT = 3


class Node:
    """
    Basic doubly linked list node
    """

    __slots__ = "_pos", "_prev", "_nextn", "_moves_bin", "_chosen"

    def __init__(
        self,
        pos: tuple[int, int] = None,
        prev: Self = None,
        nextn: Self = None,
    ):
        self._pos = pos
        self._prev = prev
        self._nextn = nextn
        self._moves_bin = set()
        self._chosen = set()


class Path:
    """
    A flavor of doubly linked list abstraction.
    Add to list when a position is chosen
    Remove from tail of list when '_backup' is called
    """

    def __init__(self) -> None:
        self._head = Node()
        self._tail = Node()
        self._head._nextn = self._tail
        self._tail._prev = self._head
        self._current = self._head

    def _add_element(self, pos: tuple[int, int]) -> Node:
        """
        As a position is chosen, it will be added to the path.

        :param pos:
        :return:
        """

        new_node = Node(pos=pos, prev=self._current, nextn=self._current._nextn)
        old_tail = self._current._nextn
        self._current._nextn = new_node
        self._current = new_node
        self._current._nextn = old_tail
        return self._current

    def _remove_element(self) -> Node:
        """
        The only remove requirement would be to backtrack from a 'no moves left' situation
        :param pos:
        :return:
        """
        self._current._prev._nextn = (
            self._current._nextn
        )
        self._current._nextn._prev = (
            self._current._prev
        )
        self._current = (
            self._current._prev
        )
        while self._current._moves_bin:
            self._current._moves_bin.pop()
        return self._current  # used

    def _path_print(self):
        """
        Prints current path and total move count
        :return:
        """
        print("*******************************START*****************************\n")
        print(f"CURRENT NODE: {self._current._pos}")
        node_print = self._head
        count = 0
        while node_print._nextn:
            count += 1
            print(f"POSITION: {node_print._pos}")
            node_print = node_print._nextn
        print(f"PATH MOVE COUNT: {count}")
        print("********************************END******************************\n")


class CastleQueenSide:
    def __init__(self, pos: tuple[int, int] = (7, 1)) -> None:
        """
        This program runs an algorithm to track the path of the Knight through the chess board array.
        The goal is to store and output the path that will allow the knight to just land on each space of the board
        only once.  The Knight does NOT land back on its starting position.

        There are a few features to be aware of:
        1. The path chosen is not completely random.  The choices are first narrowed by prioritizing the outer two
        layers of the matrix, corners in addition to a position with the most free and available moves around it
        (un-marked).  Then it was just prioritizing moves by proximity to un-marked spaces.
        2. When the path reaches a dead-end it will back-track to the position that has an available move.
        3. Despite this 'backtracking' algorithm.  The amount of available moves upon even ONE incorrect path is
        enormous.  I found it was better to backtrack by a larger chunk of moves after a certain amount of bad
        moves were found.

        :param pos:
        """
        self.board = numpy.array(8 * [8 * [OPEN]])
        self.avail_moves = set()
        self.current_pos = pos
        self.marked = set()
        self.marked.add(pos)
        self.path = Path()
        self.dead_end_count = 0
        self.last_high_move_node = None

    def _updateboard(self) -> None:
        """
        This method updates the board layout to match current field for printing purposes
        """
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                self.board[x][y] = OPEN
        for x, y in self.marked:
            self.board[x][y] = MARKED
        for x, y in self.path._current._moves_bin:
            self.board[x][y] = MOVES
        x, y = self.current_pos
        self.board[x][y] = CURRENT

    def _boardprint(self) -> None:
        """
        This method prints the current board layout to stdout using black, white, blue, and red emojis.
        :return:
        """
        self._updateboard()
        for row in self.board:
            q_print = []
            for place in row:
                if place == 0:
                    q_print.append("\U0001F535")
                elif place == 1:
                    q_print.append("\U000026AB")
                elif place == 2:
                    q_print.append("\U000026AA")
                elif place == 3:
                    q_print.append("\U0001F534")
                elif place == 4:
                    q_print.append("\U0001F7E2")

            print(q_print)

        print("\n")

    def _check_moves(self) -> None:
        """
        This method checks the available moves for the knight and adds them to the class attribute self.avail_moves
        :return: None
        """
        while self.path._current._moves_bin:
            self.path._current._moves_bin.pop()

        x, y = self.current_pos
        moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

        for xm, ym in moves:
            new_x = x + xm
            new_y = y + ym
            check_pos = (new_x, new_y)
            if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7:
                continue
            if (
                check_pos not in self.marked
                and check_pos not in self.path._current._chosen
            ):
                self.path._current._moves_bin.add((new_x, new_y))
            else:
                continue

    def _check_proximity(self) -> None:
        """
        Ranks existing available moves by their proximity to 'marked' locations
        LOWER IS BETTER
        Refines self.path._current._moves_bin and limits available
        """
        pdict = {}
        copy_moves = self.path._current._moves_bin

        proxim = [(1, 1), (1, 0), (0, 1), (-1, 1), (-1, -1), (-1, 0), (0, -1), (1, -1)]
        while self.path._current._moves_bin:
            move = self.path._current._moves_bin.pop()
            xc, yc = move[0], move[1]
            marked_count = 0
            for xp, yp in proxim:
                new_xp = xc + xp
                new_yp = yc + yp
                if (new_xp, new_yp) in self.marked:
                    marked_count += 1

            pdict[(xc, yc)] = marked_count

        mov_range = defaultdict(list)
        for key, val in pdict.items():
            mov_range[val].append(key)

        lowest = min(x for x in mov_range.keys())

        if mov_range:
            if len(mov_range[lowest]) > 1:
                for val in [x for x in mov_range[lowest]]:
                    self.path._current._moves_bin.add(val)
            else:
                self.path._current._moves_bin.add(mov_range[lowest][0])
        else:
            self.path._current._moves_bin = copy_moves

    def _outside_in(self) -> None:
        """
        This method is meant to prioritize moves along the outer perimeter of the board first.
        After a certain number of moves, it stops excluding moves through the center of the board.
        Outer Perimter: 2 layers
        """
        temp_bin = []
        moves_copy = []
        while self.path._current._moves_bin:
            move = self.path._current._moves_bin.pop()
            moves_copy.append(move)
            mx, my = move[0], move[1]
            if 2 > mx >= 0 or 5 < mx <= 7 and 2 > my >= 0 or 5 < my <= 7:
                temp_bin.append((mx, my))

        if not temp_bin:
            for item in moves_copy:
                self.path._current._moves_bin.add(item)
            del moves_copy
        else:
            for item in temp_bin:
                self.path._current._moves_bin.add(item)

    def _backup_move(self) -> tuple[int, int]:
        """
        This method removes the current node from the Path object, replacing with pointer to previous.

        :return:
        """
        old_pos = self.current_pos
        old_x, old_y = self.current_pos[0], self.current_pos[1]
        self.board[old_x][old_y] = OPEN
        new_curr = self.path._remove_element()
        self.marked.remove(old_pos)
        self.current_pos = new_curr._pos
        self.dead_end_count += 1
        self._check_moves()
        self._updateboard()
        return old_pos

    def start(self):
        """
        Location of core game logic, game start.
        :return:
        """
        start = perf_counter()
        count = 0
        bad_move_count = 0
        click_count = 0
        # Main loop - stops only when hits 64 positions in 'marked' bin
        while len(self.marked) != 64:
            # below while loop exists only to provide a loop for printing and analyzing, can be removed
            while click_count < 50:
                click_count += 1
                if len(self.marked) < 30:
                    self._check_moves()
                    self._outside_in()
                else:
                    self._check_moves()
                if self.path._current._moves_bin:
                    self._check_proximity()

                if not self.path._current._moves_bin:
                    # Every 1000 dead-end moves where Knight no longer had moves, back up 35 moves (or enter other)
                    if bad_move_count <= 1000:
                        while len(self.path._current._moves_bin) == 0:
                            self._backup_move()
                            bad_move_count += 1
                            count += 1
                    else:
                        for x in range(35):  # Alter this range to back up more/less moves at a time
                            self._backup_move()
                            count += 1
                        bad_move_count = 0

                else:
                    # Prioritize corners, many times unable to reach after rest filled
                    if (0, 0) in self.path._current._moves_bin:
                        cx, xy = 0, 0
                    elif (0, 7) in self.path._current._moves_bin:
                        cx, xy = 0, 7
                    elif (7, 0) in self.path._current._moves_bin:
                        cx, xy = 7, 0
                    elif (7, 7) in self.path._current._moves_bin:
                        cx, xy = 7, 7
                    else:
                        # Randomized choice after above move filters
                        t_choice = random.choice(
                            [x for x in self.path._current._moves_bin]
                        )
                        cx = t_choice[0]
                        xy = t_choice[1]
                    self.path._current._chosen.add((cx, xy))
                    self.path._add_element(pos=(cx, xy))
                    self.marked.add((cx, xy))
                    self.current_pos = (cx, xy)
                    self.board[cx][xy] = 1
                    # Remove comment below for visualization of board layout 'self._boardprint()'
                    # self._boardprint()
                    count += 1
            # Remove below comment on line 328 - 'input()' to be able to halt the algorithm and review print results
            # input() - remove the comment here to be able to click through and view 50 move intervals
            # Remove comments on 'self._boardprint()' to view moves
            click_count = 0

        print("YOU DID IT") # Because you did it
        self.path._path_print()
        self._boardprint()
        print(bad_move_count)
        stop = perf_counter()
        return print(f"ACTION COUNT: {count}, TIME: {stop - start:.6f}")


if __name__ == "__main__":
    # C = CastleQueenSide()
    # print(C.start())

    def counterit(number: int = 5) -> None:
        """
        Simple run, analysis tool that will run the algorithm 'number' amount of times and output minor
        statistics about the lot.
        :param number:
        :return: None
        """
        l = []
        while number:
            C = CastleQueenSide()
            start = perf_counter()
            C.start()
            stop = perf_counter()
            l.append(stop - start)
            number -= 1
        print(f"MIN: {min(l):.4f}")
        print(f"MAX: {max(l):.4f}")
        print(f"MEAN: {statistics.mean(l):.4f}")
        print(f"MEDIAN: {statistics.median(l)}")

    counterit(3)
