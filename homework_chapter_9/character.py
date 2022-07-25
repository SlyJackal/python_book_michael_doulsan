
from random import randrange




class Character_Player():

level = 1
strength = randrange(1,4)
armor = randrange(1,4)
health = randrange(10,15)


    def __init__(self, level, strenght, armor, health):
        self.level = level
        self.strenght = strenght
        self.armor = armor
        self.health = health

        
     

    def level_up(self, level, strength, armor, health):
        strength_upgrade = randrange(1,5)
        print(strength_upgrade)
        armor_upgrade = randrange(1,5)
        print(armor_upgrade)
        health_upgrade = randrange(5,10)
        print(health_upgrade)
        self.level += 1
        print(f'level = {level}')
        print(f'self.level = {self.level}')
        self.strength += strength_upgrade
        
        self.armor += armor_upgrade
        self.health += health_upgrade
        return level, strength, armor, health


        
vova = Character_Player()

print(vova.strength)







#if name == "main":
#    print("This is a module for character.")
#    input("\n\nPress the enter key to exit.")