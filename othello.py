# Othello, 2:30 start

"""
board  8x8 array

designate b, w to coordinates that have those 'discs', create methods to update based on user input, most likely
as coordinates.

attempt to use a try/except model to 'listen' for a 'game is finished' exception to stop loop for user input

https://asciinema.org/a/CtCXajLMGWqEEF4o7pdWpByBU

"""

class GameFinished(Exception):
    pass

class AgainstGameRules(Exception):
    print("You entered invalid coordinates, either a piece was there already or you didn't adhere to the game rules")
    pass

class Othello:
    def __init__(self):
        self.board = 8*[8*[0]]

    def _boardprint(self):
        for row in self.board:
            print(row)

    def _updateboard(self, x: int, y: int, black=True) -> None:
        """
        black = 2
        white = 3
        For any move the first things to check:
        X is ROW, Y is COL
        1. Is space empty, here meaning does value == 0
        2. MOVE RULES:
            2.1 - OppositePieceChecks -
                a) (x-1, y), (x+1, y), (x, y-1), (x, y+1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)

            2.2 - Check Existing Pieces at correct locations and are correct color
                b) (x-2, y), (x+2, y), (x, y-2), (x, y+2), (x-2, y-2), (x-2, y+2), (x+2, y-2), (x+2, y-2)

        """
        piece_checkdict = {
            'a': lambda x, y, d: self.board[x-1][y] == d,
            'b': self.board[x+1][y],
            'c': self.board[x][y-1],
            'd': self.board[x][y+1],
            'e': self.board[x-1][y-1],
            'f': self.board[x-1][y+1],
            'g': self.board[x+1][y-1],
            'h': self.board[x+1][y+1],
        }
        cur = self.board
        if self.board[x][y] != 0:
            raise AgainstGameRules
        if black:
            for key, val in piece_checkdict.items():



        pass

    def inputloop(self):
        while True:
            black_input = [int(x) for x in input("BLACK TURN: Please enter X Y coordinates between 0 and 7").split()]
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





        white_input = input()
        pass

    def maingame(self):
        try:
            while True:
                self.inputloop()
        except GameFinished:
            pass



if __name__ == "__main__":
    test = [int(x) for x in input().split()]
    print(type(test))
    for x in test:
        print(x)

