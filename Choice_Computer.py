import random

DIRECTIONS = ['R', 'L', 'U', 'D']

def Choice_Computer(Room, Coordinates, Size):
    X_End = False
    Y_End = False

    X_Coord = Coordinates[1]
    Y_Coord = Coordinates[0]

    Options = []

    if X_Coord == 0 or X_Coord == Size-1:
        X_End = True # If current room is at either end (x axis)
    
    if Y_Coord == 0 or Y_Coord == Size-1:
        Y_End = True # If current room is at either end (y axis)
    
    if X_End == True and Y_End == True:
        if X_Coord == 0 and Y_Coord == 0:
            Options.append(random.choice(['R', 'D']))
            Options.append(random.choice(['R', 'D']))

            if Options.count('D') > 1:
                Options = ['D']

            if Options.count('R') > 1:
                Options = ['R']
        elif X_Coord == 0 and Y_Coord == Size-1:
            Options.append(random.choice(['U', 'R']))
            Options.append(random.choice(['U', 'R']))

            if Options.count('U') > 1:
                Options = ['U']

            if Options.count('R') > 1:
                Options = ['R']
        elif X_Coord == Size-1 and Y_Coord == 0:
            Options.append(random.choice(['L', 'D']))
            Options.append(random.choice(['L', 'D']))

            if Options.count('L') > 1:
                Options = ['L']

            if Options.count('D') > 1:
                Options = ['D']
        elif X_Coord == Size-1 and Y_Coord == Size-1:
            Options.append(random.choice(['L', 'U']))
            Options.append(random.choice(['L', 'U']))

            if Options.count('L') > 1:
                Options = ['L']

            if Options.count('U') > 1:
                Options = ['U']
    elif X_End == True:
        if X_Coord == 0:
            Options.append(random.choice(['R', 'U', 'D']))
            Options.append(random.choice(['R', 'U', 'D']))

            while Options.count('R') > 1:
                Options.remove('R')

            while Options.count('U') > 1:
                Options.remove('U')

            while Options.count('D') > 1:
                Options.remove('D')
        elif X_Coord == Size-1:
            Options.append(random.choice(['L', 'U', 'D']))
            Options.append(random.choice(['L', 'U', 'D']))

            while Options.count('L') > 1:
                Options.remove('L')

            while Options.count('U') > 1:
                Options.remove('U')

            while Options.count('D') > 1:
                Options.remove('D')
    elif Y_End == True:
        if Y_Coord == 0:
            Options.append(random.choice(['R', 'L', 'D']))
            Options.append(random.choice(['R', 'L', 'D']))

            while Options.count('R') > 1:
                Options.remove('R')

            while Options.count('L') > 1:
                Options.remove('L')

            while Options.count('D') > 1:
                Options.remove('D')
        elif Y_Coord == Size-1:
            Options.append(random.choice(['L', 'U', 'R']))
            Options.append(random.choice(['L', 'U', 'R']))

            while Options.count('L') > 1:
                Options.remove('L')

            while Options.count('U') > 1:
                Options.remove('U')

            while Options.count('R') > 1:
                Options.remove('R')
    else:
        Options.append(random.choice(['L', 'U', 'R', 'D']))
        Options.append(random.choice(['L', 'U', 'R', 'D']))

        while Options.count('L') > 1:
            Options.remove('L')

        while Options.count('U') > 1:
            Options.remove('U')

        while Options.count('R') > 1:
            Options.remove('R')

        while Options.count('D') > 1:
            Options.remove('D')

    return Choice_Formatter(Options)

def Choice_Formatter(Options):
    String = 'You can go '

    if len(Options) == 1:
        if 'R' in Options:
            String += 'Right [R]. '
        elif 'U' in Options:
            String += 'Up [U]. '
        elif 'D' in Options:
            String += 'Down [D]. '
        elif 'L' in Options:
            String += 'Left [L]. '
    else:
        if 'R' in Options[0]:
            String += 'Right [R] or '
        elif 'U' in Options[0]:
            String += 'Up [U] or '
        elif 'D' in Options[0]:
            String += 'Down [D] or '
        elif 'L' in Options[0]:
            String += 'Left [L] or '
        
        if 'R' in Options[1]:
            String += 'Right [R]. '
        elif 'U' in Options[1]:
            String += 'Up [U]. '
        elif 'D' in Options[1]:
            String += 'Down [D]. '
        elif 'L' in Options[1]:
            String += 'Left [L]. '
        
    return String