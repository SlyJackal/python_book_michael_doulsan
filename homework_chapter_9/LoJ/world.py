from random import randrange

class World():
    def __init__(self):
        map_size = randrange(10, 20)
        print(f'Map Size - {map_size}')
        map = list()
        for i in range(map_size):
            map.append(i)
        print(map)

if name == "main":
    print("This is a module for world creation.")
    input("\n\nPress the enter key to exit.")