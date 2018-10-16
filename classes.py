class Player():
    def __init__(self):
        self.present = False
        self.opponents = -1
        self.stack = -1
        self.hand = [-1, -1]
        self.turn = True
        self.pf_value = -1         # 0-100
        self.street_chance = -1                     # 0-100
        self.flush_chance = -1                      # 0-100
        self.overcards = -1                         # 1 or 2


class Board():
    def __init__(self):
        self.board = [0, 0, 0, 0, 0]
        self.street = ''
        self.flop = [0, 0, 0]
        self.turn = -1
        self.river = -1
        self.pot = -1
        self.dealer = ''
