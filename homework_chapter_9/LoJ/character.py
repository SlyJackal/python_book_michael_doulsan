from random import randrange

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


        
vova = Character_Player()
print(vova.level)
print(vova.strength)
print('--------')
vova.level_up()
print('--------')
print(vova.level)
print(vova.strength)







#if name == "main":
#    print("This is a module for character.")
#    input("\n\nPress the enter key to exit.")