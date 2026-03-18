import random

def Fight(PLAYER_STATS, PLAYER_EQUIPMENT, PLAYER_ABILITIES, ENEMY_STATS, ENEMY):
    Attack = random.randint(0, 1)
    Starting_Defence = PLAYER_STATS['Defence']
    
    while PLAYER_STATS['Health'] > 0 and ENEMY_STATS['Health'] > 0:
        if Attack == 1:
            Damage = (PLAYER_STATS['Defence'] + PLAYER_EQUIPMENT['Defence']) - (ENEMY_STATS['Attack'] + random.randint(0,3))
            if Damage < 0:
                Damage = abs(Damage)
            elif Damage > 0:
                Damage = 0

            PLAYER_STATS['Health'] -= Damage

            if PLAYER_STATS['Health'] < 0:
                PLAYER_STATS['Health'] = 0

            print(f"The {ENEMY} does {Damage} damage. You are now on {PLAYER_STATS['Health']} HP")
            Attack -= 1
        else:
            Player_Turn(PLAYER_STATS, PLAYER_EQUIPMENT, PLAYER_ABILITIES, ENEMY_STATS, Starting_Defence)

            Attack += 1

def Player_Turn(PLAYER_STATS, PLAYER_EQUIPMENT, PLAYER_ABILITIES, ENEMY_STATS, Starting_Defence):
    print(f"Your Stats:")
    print(f"    Total Defence: {PLAYER_STATS['Defence'] + PLAYER_EQUIPMENT['Defence']}")
    print(f"    Total Health: {PLAYER_STATS['Health'] + PLAYER_EQUIPMENT['Health']}")
    print(f"Your Actions:")
    for index, item in enumerate(PLAYER_ABILITIES, start = 1):
        print(f'    {index}. {item}')

    choice = ''

    while not choice.isdigit() or not (0 <= (int(choice) - 1) < len(PLAYER_ABILITIES)):
         choice = input('> ')

    Ability = PLAYER_ABILITIES[int(choice) - 1]

    if Ability == 'Standard':
        Damage = ENEMY_STATS['Defence'] - (PLAYER_STATS['Attack'] + PLAYER_EQUIPMENT['Attack'])

        if Damage < 0:
            Damage = abs(Damage)
        elif Damage > 0:
            Damage = 0

        ATTACK_DATA = {
            'Attack_Type': 'standard',
            'Damage': Damage,
            'Defence_Effects': None,
            'Enemy_Health': ENEMY_STATS['Health'] - Damage,
            'Enemy_Type': ENEMY_STATS['Enemy_Type'],
        }
    elif Ability == 'Strong':
        Damage = ENEMY_STATS['Defence'] - ((PLAYER_STATS['Attack'] + PLAYER_EQUIPMENT['Attack']) + random.randint(1, 3))

        if Damage < 0:
            Damage = abs(Damage)
        elif Damage > 0:
            Damage = 0

        ATTACK_DATA = {
            'Attack_Type': 'strong',
            'Damage': Damage,
            'Defence_Effects': -2,
            'Enemy_Health': ENEMY_STATS['Health'] - Damage,
            'Enemy_Type': ENEMY_STATS['Enemy_Type'],
        }
    elif Ability == 'Jab':
        Damage = ENEMY_STATS['Defence'] - ((PLAYER_STATS['Attack'] + PLAYER_EQUIPMENT['Attack']) + random.randint(3, 6))

        if Damage < 0:
            Damage = abs(Damage)
        elif Damage > 0:
            Damage = 0

        ATTACK_DATA = {
            'Attack_Type': 'jab',
            'Damage': Damage,
            'Defence_Effects': 2,
            'Enemy_Health': ENEMY_STATS['Health'] - Damage,
            'Enemy_Type': ENEMY_STATS['Enemy_Type'],
        }     
    else:
        a = 1

    ENEMY_STATS['Health'] -= Damage
    String = Attack_Formatter(ATTACK_DATA)
    print(String)
    PLAYER_STATS['Defence'] = Starting_Defence

    if ATTACK_DATA['Defence_Effects'] != None:
        PLAYER_STATS['Defence'] += ATTACK_DATA['Defence_Effects']

def Attack_Formatter(Attack_Data):
    if Attack_Data['Enemy_Health'] < 0:
        Attack_Data['Enemy_Health'] = 0

    if Attack_Data['Defence_Effects'] != None:
        if Attack_Data['Defence_Effects'] > 0:
            return f"You execute a {Attack_Data['Attack_Type']} attack and do {Attack_Data['Damage']} damage. The {Attack_Data['Enemy_Type']} is now on {Attack_Data['Enemy_Health']} HP \nPlayer Effects: \nDefence +{Attack_Data['Defence_Effects']}"
        else:
            return f"You execute a {Attack_Data['Attack_Type']} attack and do {Attack_Data['Damage']} damage. The {Attack_Data['Enemy_Type']} is now on {Attack_Data['Enemy_Health']} HP \nPlayer Effects: \nDefence {Attack_Data['Defence_Effects']}"
    else:
        return f"You execute a {Attack_Data['Attack_Type']} attack and do {Attack_Data['Damage']} damage. The {Attack_Data['Enemy_Type']} is now on {Attack_Data['Enemy_Health']} HP \nThere is no player effect"