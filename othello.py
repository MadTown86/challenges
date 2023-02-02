# Othello, 2:30 start
import itertools
import numpy
import random
"""
board  8x8 array

designate b, w to coordinates that have those 'discs', create methods to update based on user input, most likely
as coordinates.

attempt to use a try/except model to 'listen' for a 'game is finished' exception to stop loop for user input

https://asciinema.org/a/CtCXajLMGWqEEF4o7pdWpByBU

"""

BLACK = 2
WHITE = 3
EMPTY = 0
TURN = BLACK

class GameFinished(Exception):
    pass

class AgainstGameRules(Exception):
    print("You entered invalid coordinates, either a piece was there already or you didn't adhere to the game rules")
    pass

class Othello:
    def __init__(self, computer=True):
        self.board = numpy.array(8*[8*[0]])
        self.board[3][3] = 3
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 3
        self.black = {(3, 4), (4, 3)}
        self.white = {(3, 3), (4, 4)}
        self.black_moves = []
        self.white_moves = []
        self.computer = computer

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
        self.black_moves = []
        self.white_moves = []
        # Check adjacent positions from self for existence of opposite color discs
        p_opposite = {
            'n': lambda x, y, d: self.board[x - 1][y] == d if x >= 1 else False,
            's': lambda x, y, d: self.board[x + 1][y] == d if x <= 6 else False,
            'w': lambda x, y, d: self.board[x][y - 1] == d if y >= 1 else False,
            'e': lambda x, y, d: self.board[x][y + 1] == d if y <= 6 else False,
            'nw': lambda x, y, d: self.board[x - 1][y - 1] == d if x >= 1 and y >= 1 else False,
            'ne': lambda x, y, d: self.board[x - 1][y + 1] == d if x >= 1 and y <= 6 else False,
            'sw': lambda x, y, d: self.board[x + 1][y - 1] == d if x <= 6 and y >= 1 else False,
            'se': lambda x, y, d: self.board[x + 1][y + 1] == d if x <= 6 and y <= 6 else False,
        }
        # Check for same color pieces from self position to ensure move is valid
        p_movecheck = {
            'n': lambda x, y, d: self.board[x - 2][y] == d if x >= 2 else False,
            's': lambda x, y, d: self.board[x + 2][y] == d if x <= 5 else False,
            'w': lambda x, y, d: self.board[x][y - 2] == d if y >= 2 else False,
            'e': lambda x, y, d: self.board[x][y + 2] == d if y <= 5 else False,
            'nw': lambda x, y, d: self.board[x - 2][y - 2] == d if x >= 2 and y >= 2 else False,
            'ne': lambda x, y, d: self.board[x - 2][y + 2] == d if x >= 2 and y <= 5 else False,
            'sw': lambda x, y, d: self.board[x + 2][y - 2] == d if x <= 5 and y >= 2 else False,
            'se': lambda x, y, d: self.board[x + 2][y + 2] == d if x <= 5 and y <= 5 else False,
        }
        # def moves(r, c, R, C):
        #     offsets = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not i == j == 0]
        #     return [(r + i, c + j) for i, j in offsets if 0 <= r + i < R and 0 <= c + j < C]
        # print(moves(0, 0, 10, 10))
        # print(moves(5, 5, 6, 7))

        neighbors = {
            'n': lambda x, y: (x - 1, y),
            's': lambda x, y: (x + 1, y),
            'e': lambda x, y: (x, y + 1),
            'w': lambda x, y: (x, y - 1),
            'ne': lambda x, y: (x - 1, y + 1),
            'se': lambda x, y: (x + 1, y + 1),
            'nw': lambda x, y: (x - 1, y - 1),
            'sw': lambda x, y: (x + 1, y - 1)
        }

        moves = {
            'n': lambda x, y: (x - 2, y),
            's': lambda x, y: (x + 2, y),
            'e': lambda x, y: (x, y + 2),
            'w': lambda x, y: (x, y - 2),
            'ne': lambda x, y: (x - 2, y + 2),
            'se': lambda x, y: (x + 2, y + 2),
            'nw': lambda x, y: (x - 2, y - 2),
            'sw': lambda x, y: (x + 2, y - 2)
        }
        b_ops = []
        w_ops = []
        for x, y in self.black:
            for key, val in p_opposite.items():
                if val(x, y, WHITE):
                    b_ops.append(key)
            for item in b_ops:
                if p_movecheck[item](x, y, EMPTY):
                    self.black_moves.append(moves[item](x, y))
            # for item in b_ops:
            #     if item in b_movs:
            #         self.black_moves.append(moves[item](x, y))

        for x, y in self.white:
            for key, val in p_opposite.items():
                if val(x, y, BLACK):
                    w_ops.append(key)
            for item in w_ops:
                if p_movecheck[item](x, y, EMPTY):
                    self.white_moves.append(moves[item](x, y))

        if len(self.black_moves) == 0 and TURN == BLACK:
            if len(self.black) > len(self.white):
                raise GameFinished(f'BLACK WINS: {len(self.black)}')
            else:
                raise GameFinished(f'WHITE WINS: {len(self.white)}')
        elif len(self.white_moves) == 0 and TURN == WHITE:
            if len(self.black) > len(self.white):
                raise GameFinished(f'BLACK WINS: {len(self.black)}')
            else:
                raise GameFinished(f'WHITE WINS: {len(self.white)}')



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

        # Flips over opposite color nodes between current players nodes after valid move chosen
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
                            if color == BLACK:
                                self.black.add((flipx, flipy))
                                self.white.remove((flipx, flipy))
                            else:
                                self.white.add((flipx, flipy))
                                self.black.remove((flipx, flipy))
                        break
                    if self.board[inx][iny] == opcolor:
                        flip_bin.append((inx, iny))
                        w = True
                        continue
                    if self.board[inx][iny] == color and not w:
                        break
                    if self.board[inx][iny] == 0:
                        break


        reduce_redundancy(x, y, black)

    def _computer(self):
        # Random automation of computer's choices
        for moves in self.white_moves:
            print(moves)
        if self.white_moves:
            x, y = random.choice(self.white_moves)
            print(f'WHITE CHOOSES (X, Y) - {x} {y}')
            self.board[x][y] = WHITE
            self._traverse_flip(x, y, black=False)


    def _updateboard(self, x: int, y: int, black=True) -> None:
        global TURN
        won = ''
        output = f'{won} the round! : WHITE: {len(self.white)} -- BLACK: {len(self.black)}'
        if not len(self.black_moves) or not len(self.white_moves):
            if len(self.black) > len(self.white):
                won = 'BLACK'
                print(output)
                raise GameFinished
            else:
                won = 'WHITE'
                print(output)
                raise GameFinished
        if black:
            if (x, y) in self.black_moves:
                self.board[x][y] = BLACK
                self.black.add((x, y))
                self._traverse_flip(x, y)
        elif not black:
            if (x, y) in self.black_moves:
                self.board[x][y] = BLACK
                self.white.add((x, y))
                self._traverse_flip(x, y, black=False)


    def inputloop(self):
        global TURN
        self._boardprint()
        while True:
            if TURN == BLACK:
                self._movesquery(TURN)
                try:
                    black_input = input('Please enter x, y coordinates for black move: ')
                    if black_input == 'exit':
                        exit()
                    else:
                        black_input = [int(x) for x in black_input.split()]
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
                    # try:
                    self._updateboard(black_input[0], black_input[1])
                    TURN = WHITE
                    # except AgainstGameRules:
                    #     continue
            self._boardprint()

            if TURN == WHITE:
                if not self.computer:
                    self._movesquery(TURN)
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
                    # try:
                        self._updateboard(white_input[0], white_input[1], black=False)
                    # except AgainstGameRules:
                    #     continue
                else:
                    try:
                        self._movesquery(TURN)
                        self._computer()
                        TURN = BLACK
                    except GameFinished:
                        pass

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


