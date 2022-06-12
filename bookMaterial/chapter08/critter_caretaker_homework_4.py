# Critter Caretaker
# A virtual pet to care for
import random
class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        objects = f"Your {self.name} has:\nhunger - {self.hunger}\nboredom - {self.boredom}"
        return objects  

    def __pass_time(self):
        self.hunger += random.randrange(1, 3, 1)
        self.boredom += random.randrange(1, 5, 1)

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self, food = 4):
        food = int(input(f'How much food you want to get to {self.name}?\t'))
        print("Brruppp.  Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        fun = int(input(f'How much time do you want to play with {self.name}?\t'))
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit_1 = Critter(crit_name)
    crit_name = input("What do you want to name your critter?: ")
    crit_2 = Critter(crit_name)
    crit_name = input("What do you want to name your critter?: ")
    crit_3 = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit_1.talk()
            crit_2.talk()
            crit_3.talk()
        
        # feed your critter
        elif choice == "2":
            crit_1.eat()
            crit_2.eat()
            crit_3.eat()
         
        # play with your critter
        elif choice == "3":
            crit_1.play()
            crit_2.play()
            crit_3.play()

        # secret choice
        elif choice == "4":
            print(crit_1)
            print(crit_2)
            print(crit_3)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 






