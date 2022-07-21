from random import randrange

level = 1
strength = randrange(1,4)
armor = randrange(1,4)
health = randrange(10,15)


class Character_Player():
    def __init__(self):
        self.level = 1
        self.strength = randrange(1,4)
        self.armor = randrange(1,4)
        self.health = randrange(10,15)
        return self.level, self.strength, self.armor, self.health


    def level_up(self):
        strength_upgrade = randrange(1,5)
        armor_upgrade = randrange(1,5)
        health_upgrade = randrange(5,10)
        self.level += 1
        self.strength += strength_upgrade
        self.armor += armor_upgrade
        self.health += health_upgrade
        return level, strength, armor, health


        
vova = Character_Player()

print(vova.strength)







#if name == "main":
#    print("This is a module for character.")
#    input("\n\nPress the enter key to exit.")