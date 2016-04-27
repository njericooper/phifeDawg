##Pair Of Dice
import random

class PairOfDice:
    def __init__(self):
        self.redDie =0
        self.clueDie = 0

    def get redDie(self):
        return self._redDie


    def roll(self):
        self.redDie = random.choice(range(1,7))
        self.blueDie = random.choice(range(1,7))


    def sumD(self):
         return self.redDie + self.blueDie
