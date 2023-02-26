import random

import numpy
from typing import Self
from typing import Any


class Node:
    """
    Basic doubly linked list node
    """
    __slots__ = '_pos', '_prev', '_nextn', '_moves', '_block_moves', '_moves_bin'
    def __init__(self, pos: tuple[int, int] = None, prev: Self = None, nextn: Self = None,
                 _moves: int = None, _block_moves: set[tuple, tuple] = set(), _moves_bin: set[tuple, tuple] = set()):
        self._pos = pos
        self._prev = prev
        self._nextn = nextn
        self._moves = _moves
        self._moves_bin = _moves_bin
        self._block_moves = _block_moves

class Path:
    """
    A flavor of doubly linked list abstraction
    """
    def __init__(self, current: Node = None) -> None:
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

        new_node = Node(pos = pos, prev=self._current, nextn=self._current._nextn, _moves=moves)
        self._current._nextn = new_node
        self._current = new_node
        return self._current

    def _remove_element(self, pos: tuple[int, int]) -> Node:
        """
        The only remove requirement would be to backtrack from a 'no moves left' situation

        This 'may' only become necessary if I want to build-in a backtracking mechanism to go to the last position
        which had available positions not already found bad
        :param pos:
        :return:
        """
        self._current._prev._nextn = self._current._nextn
        self._current._nextn._prev = self._current._prev
        self._current = self._current._prev
        return self._current

    def _path_print(self):
        """
        Prints current path in points
        :return:
        """
        node_print = self._head
        while node_print._nextn:
            print(node_print._pos)
            node_print = node_print._nextn
        print(node_print)



class CastleQueenSide:
    def __init__(self, pos: tuple[Any, Any] = None) -> None:
        """
        This constructor builds the chess board using numpy arrays, default filled with 0's.
        It also instantiates the following class attributes

        Class Attributes:
        self.board - numpy.array
        self.marked - set() : storing locations that have been traversed
        self.avail_moves - set(): a list of moves available from current position
        self.current_pos - tuple[int, int]: this is default (7, 3) unless given alternate input by user

        *self.bad_paths - dictionary {}: This merits additional information:
        1. This is going to store bad paths in the form of doubly linked lists for now, but this format may need to
        change.
            The path itself:
            1a. Each node will contain the position element, self.board snapshot and # of moves available
            2a. The board-snapshot will be a current copy of the board layout, this is to check that all
            circumstances that lead to a 'no moves left' exception are recorded
            3a. My hope is that by doing this, I will be able to 'record' a series of points and self.board
            snapshots that resulted in a no moves left situation and provide a check so that doing the same series of
            moves can be avoided and removed from the available list of moves at each turn.  The difficulty in this, is
            that I may have to localize the layout for this check.
            The item recorded in 'bad_paths':
            4a. So in theory if there were two moves that only had one move available and then the final move with zero
            additional moves available, the initial node on this chain that had only one move would be recorded and
            a check will be made to ensure the same point isn't chosen when the same self.board is present.
                *This may be a fruitless endeaver, as there are so many paths that can be taken, it might be a moot
                point and just cost extra overhead in time/memory.
        2. Example:
            A. self.bad_paths[(7, 2)] = [self.board]

        :param pos:
        """
        self.board = numpy.array(8*[8*[0]])
        self.avail_moves = set()
        self.block_paths = set()
        self.bad_paths = {}
        self.current_pos = (7, 1)
        self.marked = set()
        self.marked.add((7, 1))
        self.win = True if len(self.avail_moves) == 0 and len(self.marked) == 64 else False
        self.path = Path(Node(pos=pos, _moves=3))

    def _boardprint(self):
        """
        This method prints the current board layout to stdout using black, white and blue emojis.
        :return:
        """
        for x, y in self.path._current._moves_bin:
            self.board[x][y] = 2
        for x, y in self.marked:
            self.board[x][y] = 1
        if self.path._current._block_moves:
            for x, y in self.path._current._block_moves:
                self.board[x][y] = 4
        x, y = self.current_pos
        self.board[x][y] = 3
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

        print('\n')
    def _bad_pathcheck(self, arg: tuple[Any, Any]) -> bool:
        """
        Create a check that takes the x, y positional input and checks the current board layout against any
        stored layouts that have proven to be 'points of no return'

        Org algorithm: if 'exact' match then don't add the move, but I will get the rest of the program running
        before I tackle the localized self.board check.
        :return:
        """
        if arg in self.path._current._block_moves:
            return False
        else:
            return True


    def _check_moves(self) -> None:
        self.avail_moves = set()
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
            self.path._current._moves_bin.add((new_x, new_y))
        self._boardprint()

    def _backup_move(self):
        old_pos = self.current_pos
        old_x, old_y = self.current_pos[0], self.current_pos[1]
        self.board[old_x][old_y] = 0
        self.bad_paths[old_pos] = self.board
        new_curr = self.path._remove_element(self.path._current._pos)
        self.marked.remove(old_pos)
        self.current_pos = new_curr._pos
        new_curr._block_moves.add(old_pos)
        return old_pos

    def start(self):

        count = 0
        while count < 100:
            # self.path._path_print()
        # while not self.win:
            self._check_moves()
            self._boardprint()
            """
            I have to use the node itself to store the 'bad paths' data for decision making.  Its only at each
            snapshot of the board/position do the decisions matter.  After that node is removed, then the 'bad' paths
            should no longer exist on the board because the state of the game is altered.
            """
            if not self.path._current._moves_bin:
                self._backup_move()
                old = None
                while self.path._current._moves == 1:
                    old = self._backup_move()
                if self.path._current._moves >= 2 and old:
                    self.path._current._block_moves.add(old)
                count += 1
            else:
                t_choice = random.choice([x for x in self.path._current._moves_bin])
                cx = t_choice[0]
                xy = t_choice[1]
                self.path._add_element(pos=(cx, xy), moves=len(self.path._current._moves_bin))
                self.marked.add((cx, xy))
                self.current_pos = (cx, xy)
                self.board[cx][xy] = 1
                count += 1



if __name__ == "__main__":
    C = CastleQueenSide()
    C.start()




