import random

ROOM_TYPES = ['Empty', 'Enemy', 'Treasure', 'Trap']

def Generate_Dungeon(size):
    dungeon = [[None for _ in range(size)] for _ in range(size)]

    for x in range(0, size):
        for y in range(0, size):
            dungeon[x][y] = random.choice(ROOM_TYPES)

    return dungeon