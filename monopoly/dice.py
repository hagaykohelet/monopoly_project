import random
class Dice:
    @staticmethod
    def dices():
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dices = dice1, dice2
        return sum(dices)
