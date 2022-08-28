from random import randrange, triangular, sample

class CharacterPlayer():

    def __init__(self):
        self.level = 1
        self.strength = randrange(1,4)
        self.armor = randrange(1,4)
        self.max_health = randrange(10,15)
        self.health = self.max_health

    def level_up(self):
        self.level += 1
        print(f'self.level = {self.level}')
        self.strength += randrange(1,5)
        self.armor += randrange(1,5)
        self.max_health += randrange(5,10)
        print(f'Your characteristics was upgraded:\nStrenght - {self.strength}\nArmor - {self.armor}\nHealh - {self.health}')

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

if __name__ == "__main__":
    print("This is a module for character.")
    input("\n\nPress the enter key to exit.")