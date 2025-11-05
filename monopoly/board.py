from monopoly.dice import Dice
from monopoly.data import tiles_data
class Board:
    data = tiles_data
    def __init__(self):
        self.location = 0
        self.dice = Dice.dices()

    def move(self):
        self.location += self.dice
        if self.location > 40:
            self.location -= 40
        return self.location





