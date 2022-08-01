from random import randrange, triangular, sample

class CharacterPlayer():

    def __init__(self):
        self.level = 1
        self.strength = randrange(1,4)
        self.armor = randrange(1,4)
        self.health = randrange(10,15)

    def level_up(self):
        strength_upgrade = randrange(1,5)
        armor_upgrade = randrange(1,5)
        health_upgrade = randrange(5,10)
        self.level += 1
        print(f'self.level = {self.level}')
        self.strength += strength_upgrade
        self.armor += armor_upgrade
        self.health += health_upgrade

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



        
vova = CharacterPlayer()
print(f'My level - {vova.level}')
print(f'My Strenght - {vova.strength}')
print(f'My Health - {vova.health}')
i = 0
while i < 20:
    i +=1
    vova.damage_out()
print('--------')
vova.level_up()
print('--------')
print(f'My level - {vova.level}')
print(f'My Strenght - {vova.strength}')
print(f'My Health - {vova.health}')
i = 0
while i < 20:
    i +=1
    vova.damage_out()

print('--------')
print('--------')
print('--------')
print('--------')
print(sample(['red', 'blue'], counts=[4, 2], k=5))
print(sample(['red', 'blue'], counts=[4, 2], k=5))
print(sample(['red', 'blue'], counts=[4, 2], k=5))
print(sample(['red', 'blue'], counts=[4, 2], k=5))
print(sample(['red', 'blue'], counts=[4, 2], k=5))
print(sample(['red', 'blue'], counts=[4, 2], k=5))
print(sample(['red', 'blue'], counts=[4, 2], k=5))
print(sample(['red', 'blue'], counts=[4, 2], k=5))









#if name == "main":
#    print("This is a module for character.")
#    input("\n\nPress the enter key to exit.")