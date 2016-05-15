from xo.Board import Board

'''
    @class: Klasa odpowiedzialna za logikę gry
    @author: Wojciech Pitek
    @created: 15.05.2016
'''


class Game:
    PLAYERS = [Board.O, Board.X]

    def __init__(self):
        print("Kolko i krzyzyk v.0.0.1")
        self._board = Board()
        self.winner = None
        self._turn = self.PLAYERS[0]

    def start(self):
        self.turn()

    def turn(self):
        while self._board.has_available_fields() and not self.check_winner():
            print("\nRuch gracza: %s\n" % self._turn)
            x = int(input("Podaj koordynat x: "))
            y = int(input("Podaj koordynat y: "))

            if x in range(1, 4) and y in range(1, 4):
                print("Podałeś koordynaty: x = %d, y = %d" % (x, y))
                if self._board.set(x - 1, y - 1, self._turn):
                    self._board.print()
                    self.change_player()
                else:
                    print("Pole o podanych koordynatach jest już wypełnione!")
            else:
                print("Podałeś błędne koordynaty - nie mogą one być mniejsze od 1 i większe od 3")
        print("Gra skończona. Wygrał gracz %s" % self.winner)

    def change_player(self):
        self._turn = self.PLAYERS[1] if self._turn == self.PLAYERS[0] else self.PLAYERS[0]

    def check_winner(self):
        winner_pos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        ]
        for pos in winner_pos:
            if self._board.get()[pos[0]] == self._board.get()[pos[1]] and self._board.get()[pos[1]] == \
                    self._board.get()[pos[2]] and self._board.get()[pos[0]] != Board.EMPTY:
                self.winner = self.PLAYERS[0] if self._board.get()[pos[0]] == self.PLAYERS[0] else self.PLAYERS[1]
                return True
        return False
