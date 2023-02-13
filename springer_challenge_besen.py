from __future__ import annotations
from typing import Self

import numpy


class PathNode:
    __slots__ = '_pos', '_nextl', '_prev'

    def __init__(self, pos: (int, int) = None, nextl: Self = Self, prev: Self = Self) -> None:
        self._pos = pos
        self._nextl = nextl
        self._prev = prev



class CastleQueenSide:
    class PathNode:
        __slots__ = '_pos', '_nextl', '_prev'

        def __init__(self, pos: (int, int) = None, nextl: Self = None, prev: Self = None) -> None:
            self._pos = pos
            self._nextl = nextl
            self._prev = prev
    class Path:
        def __init__(self):
            self._sent_head = PathNode()
            self._sent_tail = PathNode(prev=self._sent_head)
            self._sent_head._nextl = self._sent_tail
            self._size = 0

        class Position:
            def __init__(self, container, node):
                self._container = container
                self._node = node

            def element(self):
                return self._node._pos

            def __eq__(self, other):
                return type(other) is type(self) and other._node is self._node

            def __ne__(self, other):
                return not (self == other)

        def _validate(self, p):
            if not isinstance(p, self.Position):
                raise TypeError("p must e proper Position type")
            if p._container is not self:
                raise ValueError("p does not belong to this container")
            if p._node._nextl is None:
                raise ValueError("pis no longer valid")
            return p._node

        def _make_position(self, node):  # Encapsulates the last used node
            if node is self._sent_head or node is self._sent_tail:
                return None
            else:
                return self.Position(self, node)

        def __len__(self):
            return self._size

        def is_empty(self):
            return self._size == 0

        def _insert_between(self, e, predecessor, successor):
            newest = PathNode(e, predecessor, successor)
            predecessor._nextl = newest
            successor._prev = newest
            self._size += 1
            return newest

        def _delete_node(self, node):
            predecessor = node._prev
            successor = node._nextl
            predecessor._nextl = successor
            successor._prev = predecessor
            self._size -= 1
            element = node._pos
            node._prev = node._nextl = node._pos = None
            return element
        def first(self):
            return self._make_position(self._sent_head._nextl)

        def last(self):
            return self._make_position(self._sent_tail._prev)

        def before(self, p):
            node = self._validate(p)
            return self._make_position(node._prev)

        def after(self, p):
            node = self._validate(p)
            return self._make_position(node._nextl)

        def __iter__(self):
            cursor = self.first()
            while cursor is not None:
                yield cursor.element()
                cursor = self.after(cursor)

        def add_first(self, e):
            return self._insert_between(e, self._sent_head, self._sent_head._nextl)

        def add_last(self, e):
            return self._insert_between(e, self._sent_tail._prev, self._sent_tail)

        def add_before(self, p, e):
            original = self._validate(p)
            return self._insert_between(e, original._prev, original)

        def add_after(self, p, e):
            original = self._validate(
                p
            )  # validate shells the encapsulation of Position and allows direct reference
            return self._insert_between(e, original, original._nextl)

        def delete(self, p):
            original = self._validate(p)
            return self._delete_node(original)

        def replace(self, p, e):
            original = self._validate(p)
            old_value = original._element
            original._element = e
            return old_value

    def __init__(self):
        self.board = numpy.array(8 * [8 * [0]])
        self.moves_bin = []
        self.false_moves = {}  # This is going to be tuples of (from [x, y] to [x, y], may





