import random

ENEMIES = ['goblin', 'skeleton', 'bug']
TRAPS = ['spike pit', 'hall of arrows']

def Room_Populator(Type):
    if Type == 'Empty':
        return None, None, 'This room is empty'
    elif Type == 'Enemy':
        return Enemy_Populator()
    elif Type == 'Treasure':
        return None, None, 'There is treasure in this room'
    elif Type == 'Trap':
        return Trap_Populator()

def Enemy_Populator():
    Enemy = random.choice(ENEMIES)

    return Enemy, None, f'There is a {Enemy} in this room'

def Trap_Populator():
    Trap = random.choice(TRAPS)

    return None, Trap, None