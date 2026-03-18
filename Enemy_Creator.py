import random

GOBLIN = {
    'Health': 0,
    'Defence': 3,
    'Attack': 5,
    'Enemy_Type': 'goblin',
}

SKELETON = {
    'Health': 0,
    'Defence': 2,
    'Attack': 3,
    'Enemy_Type': 'skeleton',
}

BUG = {
    'Health': 0,
    'Defence': 1,
    'Attack': 2,
    'Enemy_Type': 'bug',
}

def Enemy_Creator(Type):
    if Type == 'bug':
        ENEMY = BUG
        ENEMY['Health'] = random.randint(3, 5)
        return ENEMY
    elif Type == 'skeleton':
        ENEMY = SKELETON
        ENEMY['Health'] = random.randint(4, 8)
        return ENEMY
    elif Type == 'goblin':
        ENEMY = GOBLIN
        ENEMY['Health'] = random.randint(6, 11)
        return ENEMY