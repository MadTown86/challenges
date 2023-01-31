# Othello, 2:30 start
import itertools
import numpy
"""
board  8x8 array

designate b, w to coordinates that have those 'discs', create methods to update based on user input, most likely
as coordinates.

attempt to use a try/except model to 'listen' for a 'game is finished' exception to stop loop for user input

https://asciinema.org/a/CtCXajLMGWqEEF4o7pdWpByBU

"""

BLACK = 2
WHITE = 3
TURN = BLACK

class GameFinished(Exception):
    pass

class AgainstGameRules(Exception):
    print("You entered invalid coordinates, either a piece was there already or you didn't adhere to the game rules")
    pass

class Othello:
    def __init__(self):
        self.board = numpy.array(8*[8*[0]])
        self.board[3][3] = 3
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 3



    def _boardprint(self):

        for row in self.board:
            q_print = []
            for place in row:

                if place == 0:
                    q_print.append("\U0001F535")
                elif place == 2:
                    q_print.append("\U000026AB")
                else:
                    q_print.append("\U000026AA")
            print(q_print)
    def _movesquery(self, TURN):
        if TURN == BLACK:
            x, y = 0, 0


    def _traverse_flip(self, x: int, y: int, black=True) -> None:
        # Traverses all directions from given point and flips any that fit the rule
        direct_dict = {
            'n': lambda x, y: itertools.zip_longest(range(x-1, -1, -1), '', fillvalue=y) if x >= 1 else [(0, y)],
            's': lambda x, y: itertools.zip_longest(range(x+1, 8, 1), '', fillvalue=y) if x <= 6 else [(7, y)],
            'e': lambda x, y: itertools.zip_longest(range(y+1, 8, 1), '', fillvalue=x) if y <= 6 else [(x, 7)],
            'w': lambda x, y: itertools.zip_longest(range(y-1, -1, -1), '', fillvalue=x) if y >= 1 else [(x, 0)],
            'ne': lambda x, y: zip(range(x-1, -1, -1), range(y+1, 8, 1)) if x >= 1 and y <= 6 else [(0, 7)],
            'se': lambda x, y: zip(range(x+1, 8, 1), range(y+1, 8, 1)) if x <= 6 and y <= 6 else [(7, 7)],
            'nw': lambda x, y: zip(range(x-1, -1, -1), range(y-1, -1, -1)) if x >= 1 and y > 1 else [(0, 0)],
            'sw': lambda x, y: zip(range(x+1, 8, 1), range(y-1, -1, 1)) if x <= 6 and y > 1 else [(7, 0)]
        }

        def reduce_redundancy(x: int, y: int, black=True):
            if black:
                color = BLACK
                opcolor = WHITE
            else:
                color = WHITE
                opcolor = BLACK
            for key, val in direct_dict.items():
                w = False
                flip_bin = []
                for inx, iny in val(x, y):
                    if self.board[inx][iny] == color and w:
                        for flipx, flipy in flip_bin:
                            self.board[flipx][flipy] = color
                        break
                    if self.board[inx][iny] == color and not w:
                        break
                    if self.board[inx][iny] == 0:
                        break
                    elif self.board[inx][iny] == opcolor:
                        w = True
                        continue

        reduce_redundancy(x, y, black)

    def _updateboard(self, x: int, y: int, black=True) -> None:
        global TURN
        """
        U+26AB	- black circle
        U+26AA	- whtie circle
        U+1F7E5	- red square
        black = 2
        white = 3
        """
        # Check for adjacent pieces, ensuring opposite color
        p_opposite = {
            'n': lambda x, y, d: self.board[x-1][y] == d if x >= 1 else False,
            's': lambda x, y, d: self.board[x+1][y] == d if x <= 6 else False,
            'w': lambda x, y, d: self.board[x][y-1] == d if y >= 1 else False,
            'e': lambda x, y, d: self.board[x][y+1] == d if y <= 6 else False,
            'nw': lambda x, y, d: self.board[x-1][y-1] == d if x >= 1 and y >= 1 else False,
            'ne': lambda x, y, d: self.board[x-1][y+1] == d if x >= 1 and y <= 6 else False,
            'sw': lambda x, y, d: self.board[x+1][y-1] == d if x <= 6 and y >= 1 else False,
            'se': lambda x, y, d: self.board[x+1][y+1] == d if x <= 6 and y <= 6 else False,
        }
        # Check for
        p_movecheck = {
            'n': lambda x, y, d: self.board[x-2][y] == d if x >= 2 else False,
            's': lambda x, y, d: self.board[x+2][y] == d if x <= 5 else False,
            'w': lambda x, y, d: self.board[x][y-2] == d if y >= 2 else False,
            'e': lambda x, y, d: self.board[x][y+2] == d if y <= 5 else False,
            'nw': lambda x, y, d: self.board[x-2][y-2] == d if x >= 2 and y >= 2 else False,
            'ne': lambda x, y, d: self.board[x-2][y+2] == d if x >= 2 and y <= 5 else False,
            'sw': lambda x, y, d: self.board[x+2][y-2] == d if x <= 5 and y >= 2 else False,
            'se': lambda x, y, d: self.board[x+2][y+2] == d if x <= 5 and y <= 5 else False,
        }

        neighbors = {
            'n': lambda x, y: (x-1, y),
            's': lambda x, y: (x+1, y),
            'e': lambda x, y: (x, y+1),
            'w': lambda x, y: (x, y-1),
            'ne': lambda x, y: (x-1, y+1),
            'se': lambda x, y: (x+1, y+1),
            'nw': lambda x, y: (x-1, y-1),
            'sw': lambda x, y: (x+1, y-1)
        }

        p_opbasket = []
        m_mcbasket = []
        move = False

        if self.board[x][y] != 0:
            raise AgainstGameRules
        if black:
            for key, val in p_opposite.items():
                if val(x, y, WHITE):
                    p_opbasket.append(key)
            for key, val in p_movecheck.items():
                if val(x, y, BLACK):
                    m_mcbasket.append(key)
            for a in m_mcbasket:
                if a in p_opbasket:
                    self.board[x][y] = BLACK
                    self.board[*neighbors[a](x, y)] = BLACK
                    self._traverse_flip(x, y)
                    move = True
                    TURN = WHITE
                    break
                else:
                    continue
            if not move:
                raise AgainstGameRules()
        else:
            for key, val in p_opposite.items():
                if val(x, y, BLACK):
                    p_opbasket.append(key)
            for key, val in p_movecheck.items():
                if val(x, y, WHITE):
                    m_mcbasket.append(key)
            for a in m_mcbasket:
                if a in p_opbasket:
                    self.board[x][y] = WHITE
                    self.board[*neighbors[a](x, y)] = WHITE
                    self._traverse_flip(x, y, black=False)
                    move = True
                    TURN = BLACK
                else:
                    continue
            if not move:
                raise AgainstGameRules()

    def inputloop(self):
        self._boardprint()
        while True:
            if TURN == BLACK:
                try:
                    black_input = [int(x) for x in input("BLACK TURN: Please enter X Y coordinates between 0 and 7").split()]
                except ValueError:
                    print('You entered invalid characters, please try again.  No comma necessary to separate integers')
                    continue
                if len(black_input) != 2:
                    print("Please enter just 2 values, one for X and one for Y separated by a space, nothing else")
                    continue
                elif black_input[0] < 0 or black_input[0] > 7 or black_input[1] < 0 or black_input[1] > 7:
                    print("Please enter in values between 0 and 7")
                    continue
                else:
                    try:
                        self._updateboard(black_input[0], black_input[1])
                    except AgainstGameRules:
                        continue
            self._boardprint()

            if TURN == WHITE:
                try:
                    white_input = [int(x) for x in input("WHITE TURN: Please enter X Y coordinates between 0 and 7").split()]
                except ValueError:
                    print("Please only enter integers, no other characters allowed")
                    continue
                if len(white_input) != 2:
                    print("Please enter just 2 values, one for X and one for Y separated by a space, nothing else")
                    continue
                elif white_input[0] < 0 or white_input[0] > 7 or white_input[1] < 0 or white_input[1] > 7:
                    print("Please enter in values between 0 and 7")
                    continue
                else:
                    try:
                        self._updateboard(white_input[0], white_input[1], black=False)
                    except AgainstGameRules:
                        continue

            self._boardprint()

    def maingame(self):
        try:
            while True:
                self.inputloop()
        except GameFinished:
            pass



if __name__ == "__main__":
    C = Othello()
    C.maingame()


