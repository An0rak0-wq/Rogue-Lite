import random

from Dungeon_Generator import Generate_Dungeon
from Choice_Computer import Choice_Computer
from Main_Menu import Main_Menu
from Movement_Logic import New_Coords
from Room_Populator import Room_Populator
from Enemy_Creator import Enemy_Creator
from Fight import Fight
from Trap import Trap

LEVEL_INFO = {
    'Size': 5,
}

PLAYER_STATS = {
    'Health': 9999,
    'Attack': 3,
    'Defence': 3,
    'Gold': 0,
}

PLAYER_EQUIPMENT = {
    'Health': 0,
    'Attack': 2,
    'Defence': 0,
}

PLAYER_ABILITIES = ['Standard', 'Strong', 'Jab']

while PLAYER_STATS['Health'] > 0:
    Choice = Main_Menu()

    if Choice == '1':
        Dungeon = Generate_Dungeon(LEVEL_INFO['Size'])
        Coordinates = [0, 0]

        while PLAYER_STATS['Health'] > 0:
            Room = Dungeon[Coordinates[0]][Coordinates[1]]

            Enemy, Trap_Type, Room_String = Room_Populator(Room)
            
            if Room_String != None:
                print(Room_String)

            if Room == 'Treasure':
                Gold = int(random.uniform(0, 1) ** 2 * 24) + 1 #gives gold from 1 to 25 pieces, weighted heavily towards 1
                PLAYER_STATS['Gold'] += Gold
                print(f'You open the treasure chest, and within you find {Gold} gold. You now have {PLAYER_STATS["Gold"]} gold.')
                Dungeon[Coordinates[0]][Coordinates[1]] = 'Empty'

            if Enemy != None:
                ENEMY_STATS = Enemy_Creator(Enemy)

                Fight(PLAYER_STATS, PLAYER_EQUIPMENT, PLAYER_ABILITIES, ENEMY_STATS, Enemy)

            if Trap_Type != None:
                PLAYER_STATS, Damage_String = Trap(PLAYER_STATS, Trap_Type)

                print(Damage_String)

            print(f'Coordinates: X{Coordinates[1]} Y{Coordinates[0]}')

            print(Choice_Computer(Room, Coordinates, LEVEL_INFO['Size']))
            Coordinates = New_Coords(input('> ').strip().upper(), Coordinates)

            if Coordinates[0] == 4 and Coordinates[1] == 4:
                print('You have reached the end of this dungeon. Before you stand three options:'
                      'First, the red gate. Within must lie a powerful boss. Beat him and you will be'
                      'duly rewarded. Second, the blue gate, the gate of the weak. For those who do not'
                      'wish to test themselves against the worst this realm has to offer, you may'
                      'enter this gate, and the dungeon shall be renewed. Finally, the black gate.'
                      'Walk through this gate, and all life will cease to end. Enter your choice: ')
    elif Choice == '2':
        print('Just play the game')