from random import randrange, triangular

class Enemie():
    def __init__(self, multiplier = 1):
        self.level = multiplier
        self.strength = randrange(1,4) * level
        self.armor = randrange(1,4) * level
        self.health = randrange(10,15) * level

    def damage_out(self):
        random_rate = triangular(0.5, 2)
        level_rate = self.level * triangular(0.1, 1)
        damage_out = self.strength * random_rate + level_rate
        damage_out = int(damage_out)
        return damage_out

    def damage_in(self, enemie_damage):
        armor_rate = self.armor * triangular(0.6, 1)
        armor_rate = int(armor_rate)
        damage_in = enemie_damage * armor_rate
        return damage_in
 

