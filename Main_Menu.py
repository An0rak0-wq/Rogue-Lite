OPTIONS = ['Start', 'How To Play']

def Main_Menu():
    for index, item in enumerate(OPTIONS, start = 1):
        print(f'{index}. {item}')

    return input('> ')