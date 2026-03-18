def New_Coords(Choice, Coordinates):
    if Choice == 'U':
        Coordinates[0] -= 1
    elif Choice == 'D':
        Coordinates[0] += 1
    elif Choice == 'R':
        Coordinates[1] += 1
    elif Choice == 'L':
        Coordinates[1] -= 1

    return Coordinates