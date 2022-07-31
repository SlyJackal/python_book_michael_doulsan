from random import randrange

class Enemie():
    def __init__(self, multiplier = 1):
        self.multiplier = multiplier
        self.level *= multiplier
        self.strength = randrange(1,4) * multiplier
        self.armor = randrange(1,4) * multiplier
        self.health = randrange(10,15) * multiplier
 

