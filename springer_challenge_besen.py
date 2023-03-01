import random

import numpy
from typing import Self

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
    A flavor of doubly linked list abstraction
    """

    def __init__(self) -> None:
        self._head = Node()
        self._tail = Node()
        self._head._nextn = self._tail
        self._tail._prev = self._head
        self._current = self._head

    def _add_element(self, pos: tuple[int, int], moves: int = None) -> Node:
        """
        As a position is chosen, it will be added to the path.

        As of right now I am making it return the self.current node but may remove it as unnecessary
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

        This 'may' only become necessary if I want to build-in a backtracking mechanism to go to the last position
        which had available positions not already found bad
        :param pos:
        :return:
        """
        self._current._prev._nextn = self._current._nextn # Removing prior nodes connection to existing node
        self._current._nextn._prev = self._current._prev # Removing following node's connection to existing node
        self._current = self._current._prev # Altering the paths self._current to become the previous node
        while self._current._moves_bin: # Removing its current bin for updating
            self._current._moves_bin.pop()
        return self._current

    def _path_print(self):
        """
        Prints current path in points
        :return:
        """
        print("*******************************START*****************************\n")
        print(f'CURRENT NODE: {self._current._pos}')
        node_print = self._head
        while node_print._nextn:
            print(f'POSITION: {node_print._pos}')
            print(f'CHOSEN ON NODE: {node_print._chosen}')
            node_print = node_print._nextn
        print(node_print._pos)
        print("********************************END******************************\n")
    pass


class CastleQueenSide:
    def __init__(self, pos: tuple[int, int] = None) -> None:
        """
        This program runs an algorithm to track the path of the Knight through the chess board array.
        The goal is to store and output the path that will allow the knight to just land on each space of the board
        only once.

        :param pos:
        """
        self.board = numpy.array(8 * [8 * [OPEN]])
        self.avail_moves = set()
        self.current_pos = (7, 1)
        self.marked = set()
        self.marked.add((7, 1))
        self.win = (
            True if len(self.avail_moves) == 0 and len(self.marked) == 64 else False
        )
        self.path = Path()
        self.dead_end_count = 0
        self.last_high_move_node = None

    def _high_option_return(self):
        self.path._current._prev._nextn = self.last_high_move_node

        """
        
        :param Node: 
        :return: 
        """

    def _updateboard(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                self.board[x][y] = OPEN
        for x, y in self.marked:
            self.board[x][y] = MARKED
        for x, y in self.path._current._moves_bin:
            self.board[x][y] = MOVES
        x, y = self.current_pos
        self.board[x][y] = CURRENT

    def _boardprint(self):
        """
        This method prints the current board layout to stdout using black, white and blue emojis.
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
        while self.path._current._moves_bin:
            self.path._current._moves_bin.pop()
        """
        This method checks the available moves for the knight and adds them to the class attribute self.avail_moves

        :return: None
        """
        x, y = self.current_pos
        moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]

        for xm, ym in moves:
            new_x = x + xm
            new_y = y + ym
            check_pos = (new_x, new_y)
            if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7:
                continue
            if (
                check_pos not in self.marked and check_pos not in self.path._current._chosen
            ):
                self.path._current._moves_bin.add((new_x, new_y))
            else:
                continue


    def _backup_move(self):
        """
        This method removes the current node from the Path object, replacing with pointer to previous.
        Sets old.current position on board to 0 (empty)
        :return:
        """
        print(f'BACKED UP ONE \nOLD POS: {self.current_pos}')
        old_pos = self.current_pos
        old_x, old_y = self.current_pos[0], self.current_pos[1]
        self.board[old_x][old_y] = OPEN
        new_curr = self.path._remove_element()
        self.marked.remove(old_pos)
        self.current_pos = new_curr._pos
        self.dead_end_count += 1
        self._updateboard()
        return old_pos

    def start(self):
        count = 0
        while len(self.marked) != 45:
            input()
            print(len(self.marked))
            print(type(self.marked))
            # self.path._path_print()
            self._check_moves()
            self._boardprint()
            """
            I have to use the node itself to store the 'bad paths' data for decision making.  Its only at each
            snapshot of the board/position do the decisions matter.  After that node is removed, then the 'bad' paths
            should no longer exist on the board because the state of the game is altered.
            """
            if not self.path._current._moves_bin:
                while self.dead_end_count < 30:
                    print("***************** DEAD END *******************")
                    self._backup_move()
                    print(f'BOARD AFTER BACKUP: {count}')
                    self._boardprint()
                    count += 1
                self._high_option_return()
            else:
                # print(f'MAKING A MOVE')
                t_choice = random.choice([x for x in self.path._current._moves_bin])
                cx = t_choice[0]
                xy = t_choice[1]
                self.path._current._chosen.add((cx, xy))
                self.path._add_element(
                    pos=(cx, xy), moves=len(self.path._current._moves_bin)
                )
                self.marked.add((cx, xy))
                self.current_pos = (cx, xy)
                self.board[cx][xy] = 1
                print(f'BOARD AFTER RANDOM MOVE: {count}')
                self._boardprint()
                count += 1
        print("YOU DID IT")
        return count


if __name__ == "__main__":
    C = CastleQueenSide()
    print(C.start())

