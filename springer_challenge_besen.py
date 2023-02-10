import numpy

class CastleQueenSide:

    class PathNode:
        __slots__ = 'pos', 'next', 'prev'
        def __init__(self, pos: (int, int) = None, next:object = None, prev: object = None):
            self.pos = pos
            self.next = next
            self.prev = prev




    def __init__(self):
        self.board = numpy.array(8*[8*[0]])
        self.moves_bin = []
        self.false_moves = []  # This is going to be tuples of (from [x, y]

    class PathInNodes:
        def __init__(self):
            self.head = self.PathNode()
