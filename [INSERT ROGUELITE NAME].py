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
    'Health': 10,
    'Attack': 3,
    'Defence': 3,
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
        print(Dungeon)
        Coordinates = [0, 0]

        while PLAYER_STATS['Health'] > 0:
            Room = Dungeon[Coordinates[0]][Coordinates[1]]

            Enemy, Trap_Type, Room_String = Room_Populator(Room)
            
            if Room_String != None:
                print(Room_String)

            if Enemy != None:
                ENEMY_STATS = Enemy_Creator(Enemy)

                Fight(PLAYER_STATS, PLAYER_EQUIPMENT, PLAYER_ABILITIES, ENEMY_STATS, Enemy)

            if Trap_Type != None:
                PLAYER_STATS, Damage_String = Trap(PLAYER_STATS, Trap_Type)

                print(Damage_String)

            print(f'Coordinates: X{Coordinates[1]} Y{Coordinates[0]}')

            print(Choice_Computer(Room, Coordinates, LEVEL_INFO['Size']))
            Coordinates = New_Coords(input('> ').strip().upper(), Coordinates)
    elif Choice == '2':
        print('Just play the game')