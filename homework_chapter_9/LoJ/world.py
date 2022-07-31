from random import randrange

class World():
    def __init__(self):
        map_size = randrange(10, 20)
        print(f'Map Size - {map_size}')
        world = list()
        for i in range(map_size):
            world.append(i)
        print(world)


hell = World()

