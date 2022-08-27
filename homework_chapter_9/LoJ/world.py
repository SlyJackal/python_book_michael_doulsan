from random import randrange

class World():
    def __init__(self):
        map_size = randrange(10, 20)
        print(f'Map Size - {map_size}')
        map = list(range(map_size))
        print(map)

if name == "main":
    print("This is a module for world creation.")
    input("\n\nPress the enter key to exit.")