# Othello, 2:30 start
import itertools
import numpy
import random
"""
First implementation of game Othello.
Can be played with 0-2 human players.

Where it can be refactored for my future self.  

Explanation of why I started doing it this way:
1. Without altering the entire structure, it can be simplified in the following ways:
    a) Instead of using black=True or False to designate the current color and then also using a global TURN
        -Make it one or the other, most likely the global variable as it would be more explicit
    b) Combining the methods used to calculate the 'bins' and also traversing to flip the colors.
2. I believe all of the lambda's create a lot of overhead.  Coming from a manufacturing background and using cartesian
coordinate system.  It is a mental leap to process
"""


BLACK = 2
WHITE = 3
EMPTY = 0  # BLUE
TURN = BLACK


class GameFinished(Exception):
    def __init__(self, black: int, white: int, won: 'str') -> None:
        super().__init__()
        self.black = black
        self.white = white
        self.won = won
        self.msgs = [
            f'BLACK PIECES: {black}',
            f'WHITE PIECES: {white}',
            f'WON: {won}'
        ]

class AgainstGameRules(Exception):
    def __init__(self):
        self.msg = "You entered invalid coordinates, either a piece was there already or you didn't adhere to the game rules"

class Othello:

    def __init__(self):
        """
        Class Constructor:
        This sets the 8x8 board as a nested array using numpy.array.

        The board starts with 2 black and 2 white pieces in alternating sequence at the
        center 4 squares (3, 3) - (4, 4)
        """
        self.board = numpy.array(8*[8*[0]])
        self.board[3][3] = 3
        self.board[3][4] = 2
        self.board[4][3] = 2
        self.board[4][4] = 3
        self.black = {(3, 4), (4, 3)}
        self.white = {(3, 3), (4, 4)}
        self.black_moves = []
        self.white_moves = []
        self.computer_b = False
        self.computer_w = False
        self.won = None

    def _boardprint(self):
        """
        This method prints the current board layout to stdout using black, white and blue emojis.
        :return:
        """
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
        """
        Method calculates all potential moves for black and white pieces, becoming bins to verify user input
        or choices for computer players
        :param TURN: this is the current active turn whether BLACK or WHITE
        :return: None
        """
        self.black_moves = []
        self.white_moves = []
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

        direct_dict = {
            'n': lambda x, y: itertools.zip_longest(range(x - 1, -1, -1), '', fillvalue=y) if x >= 1 else [(0, y)],
            's': lambda x, y: itertools.zip_longest(range(x + 1, 8, 1), '', fillvalue=y) if x <= 6 else [(7, y)],
            'e': lambda x, y: itertools.zip_longest('', range(y + 1, 8, 1), fillvalue=x) if y <= 6 else [(x, 7)],
            'w': lambda x, y: itertools.zip_longest('', range(y - 1, -1, -1), fillvalue=x) if y >= 1 else [(x, 0)],
            'ne': lambda x, y: zip(range(x - 1, -1, -1), range(y + 1, 8, 1)) if x >= 1 and y <= 6 else [(0, 7)],
            'se': lambda x, y: zip(range(x + 1, 8, 1), range(y + 1, 8, 1)) if x <= 6 and y <= 6 else [(7, 7)],
            'nw': lambda x, y: zip(range(x - 1, -1, -1), range(y - 1, -1, -1)) if x >= 1 and y >= 1 else [(0, 0)],
            'sw': lambda x, y: zip(range(x + 1, 8, 1), range(y - 1, -1, -1)) if x <= 6 and y >= 1 else [(7, 0)]
        }

        b_ops = []
        w_ops = []
        for x, y in self.black:
            for key, val in p_opposite.items():
                if val(x, y, WHITE):
                    b_ops.append(key)
                if b_ops:
                    item = b_ops.pop(0)
                    for a, b in direct_dict[item](x, y):
                        if self.board[a][b] == EMPTY:
                            self.black_moves.append((a, b))
                            break
                        if self.board[a][b] == BLACK:
                            break

        for x, y in self.white:
            for key, val in p_opposite.items():
                if val(x, y, BLACK):
                    w_ops.append(key)
                if w_ops:
                    item = w_ops.pop(0)
                    for a, b in direct_dict[item](x, y):
                        if self.board[a][b] == EMPTY:
                            self.white_moves.append((a, b))
                            break
                        if self.board[a][b] == BLACK:
                            continue
                        if self.board[a][b] == WHITE:
                            break


        # This is where end-game conditions are checked
        if len(self.black_moves) == 0 and TURN == BLACK:
            if len(self.black) > len(self.white):
                raise GameFinished(black=len(self.black), white=len(self.white), won='BLACK')
            else:
                raise GameFinished(black=len(self.black), white=len(self.white), won='WHITE')
        elif len(self.white_moves) == 0 and TURN == WHITE:
            if len(self.black) > len(self.white):
                raise GameFinished(black=len(self.black), white=len(self.white), won='BLACK')
            else:
                raise GameFinished(black=len(self.black), white=len(self.white), won='BLACK')

    def _traverse_flip(self, x: int, y: int, black=True) -> None:
        """
        This method takes the current active position (x, y) and
        :param x:
        :param y:
        :param black:
        :return:
        """
        direct_dict = {
            'n': lambda x, y: itertools.zip_longest(range(x-1, -1, -1), '', fillvalue=y) if x >= 1 else [(0, y)],
            's': lambda x, y: itertools.zip_longest(range(x+1, 8, 1), '', fillvalue=y) if x <= 6 else [(7, y)],
            'e': lambda x, y: itertools.zip_longest('', range(y+1, 8, 1), fillvalue=x) if y <= 6 else [(x, 7)],
            'w': lambda x, y: itertools.zip_longest('', range(y-1, -1, -1), fillvalue=x) if y >= 1 else [(x, 0)],
            'ne': lambda x, y: zip(range(x-1, -1, -1), range(y+1, 8, 1)) if x >= 1 and y <= 6 else [(0, 7)],
            'se': lambda x, y: zip(range(x+1, 8, 1), range(y+1, 8, 1)) if x <= 6 and y <= 6 else [(7, 7)],
            'nw': lambda x, y: zip(range(x-1, -1, -1), range(y-1, -1, -1)) if x >= 1 and y >= 1 else [(0, 0)],
            'sw': lambda x, y: zip(range(x+1, 8, 1), range(y-1, -1, -1)) if x <= 6 and y >= 1 else [(7, 0)]
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
                    if self.board[inx][iny] == 0:
                        break
                    if self.board[inx][iny] == color and not w:
                        break
                    if self.board[inx][iny] == opcolor:
                        flip_bin.append((inx, iny))
                        w = True
                        continue
                    if self.board[inx][iny] == color and w:
                        if flip_bin:
                            for flipx, flipy in flip_bin:
                                self.board[flipx][flipy] = color
                                if color == BLACK:
                                    self.black.add((flipx, flipy))
                                    self.white.remove((flipx, flipy))
                                else:
                                    self.white.add((flipx, flipy))
                                    self.black.remove((flipx, flipy))
                        break

        reduce_redundancy(x, y, black)

    def _computer(self):
        # Random automation of computer's choices
        global TURN
        if TURN == BLACK:
            color = BLACK
            c_text = 'BLACK'
            c_moves = self.black_moves
            c_pos = self.black
            color_bool = True
            opp_col = WHITE
        else:
            color = WHITE
            c_text = 'WHITE'
            c_moves = self.white_moves
            c_pos = self.white
            color_bool = False
            opp_col = BLACK
        if c_moves:
            x, y = random.choice(c_moves)
            print(f'{c_text} CHOOSES (X, Y) - {x}, {y}')
            self.board[x][y] = color
            c_pos.add((x, y))
            self._traverse_flip(x, y, black=color_bool)
            TURN = opp_col

    # Verifies moves, alters choice color, adds position to self, calls method to flip others, checks for win state
    def _updateboard(self, x: int, y: int, black=True) -> None:
        global TURN
        if black:
            if (x, y) in self.black_moves:
                self.board[x][y] = BLACK
                self.black.add((x, y))
                self._traverse_flip(x, y)
                TURN = WHITE
            else:
                raise AgainstGameRules
        elif not black:
            if (x, y) in self.white_moves:
                self.board[x][y] = WHITE
                self.white.add((x, y))
                self._traverse_flip(x, y, black=False)
                TURN = BLACK

    # User input and TURN selected or TURN alternator and computer player
    def inputloop(self):
        global TURN
        self._boardprint()
        try:
            while True:
                if TURN == BLACK:
                    if not self.computer_b:
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
                            self._updateboard(black_input[0], black_input[1])
                    else:
                        self._movesquery(TURN)
                        self._computer()
                self._boardprint()

                if TURN == WHITE:
                    if not self.computer_w:
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
                            self._updateboard(white_input[0], white_input[1], black=False)
                    else:
                        self._movesquery(TURN)
                        self._computer()
                    self._boardprint()
        except GameFinished as gf:
            for msg in gf.msgs:
                print(msg)
            exit()

    def maingame(self):
        while True:
            game_set = input("Please choose how many computers will be playing between 0, 1 and 2")
            if not game_set.isnumeric():
                print("Incorrect value's entered")
            else:
                gsi = game_set
                if gsi == '0':
                    break
                if gsi == '1':
                    self.computer_w = True
                    break
                if gsi == '2':
                    self.computer_w = True
                    self.computer_b = True
                    break
                else:
                    print("Incorrect value's entered")
                    continue

        try:
            while True:
                self.inputloop()
        except GameFinished:
            exit()



if __name__ == "__main__":
    C = Othello()
    C.maingame()


