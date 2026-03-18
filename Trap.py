import random

def Trap(PLAYER_STATS, Type):
    if Type == 'spike pit':
        Damage = random.randint(1, 3)
        PLAYER_STATS['Health'] -= Damage
        Damage_String = String_Generator('spike pit', Damage, PLAYER_STATS['Health'])
        return PLAYER_STATS, Damage_String
    elif Type == 'hall of arrows':
        Damage = random.randint(2, 5)
        PLAYER_STATS['Health'] -= Damage
        Damage_String = String_Generator('shall of arrows', Damage, PLAYER_STATS['Health'])
        return PLAYER_STATS, Damage_String

        

def String_Generator(Type, Damage, HP):
    if Type == 'spike pit':
        return f'You fell in a spike pit and took {Damage} damage. You are now on {HP} HP'
    elif Type == 'hall of arrows':
        return f'You walked blindly into a hall of arrows and took {Damage} damage. You are now on {HP} HP'