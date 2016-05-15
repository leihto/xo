'''
    @class: Klasa odpowiedzialna za obsługe pola gry
    @author: Wojciech Pitek
    @created: 15.05.2016
'''

class Board:
    X = 'X'
    O = 'O'
    EMPTY = ' '

    def __init__(self):
        self.board = [self.EMPTY] * 9

    def get(self):
        return self.board[:]

    def set(self, x, y, what):
        assert x in range(0, 3)
        assert y in range(0, 3)
        assert what in [self.X, self.O]

        if self.is_empty(x, y):
            self.board[3 * x + y] = what
            return True
        else:
            return False

    def is_empty(self, x, y):
        return self.board[3 * x + y] == self.EMPTY

    def has_available_fields(self):
        for x in range(0, 8):
            if self.board[x] == self.EMPTY:
                return True
        return False

    def print(self):
        print(" %s | %s | %s \n"
              " %s | %s | %s \n"
              " %s | %s | %s " % tuple(self.board))
