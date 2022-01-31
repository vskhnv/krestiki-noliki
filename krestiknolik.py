pole = ['-','-','-','-','-','-','-','-','-']
igra = True
winner = None
player = 'X'

def doska():
    print('  1 2 3')
    print('1 ' + pole[0] + ' ' + pole[1] + ' ' + pole[2])
    print('2 ' + pole[3] + ' ' + pole[4] + ' ' + pole[5])
    print('3 ' + pole[6] + ' ' + pole[7] + ' ' + pole[8])

def play():
    doska()
    while igra:
        hod(player)
        gameover()
        turn()

    if winner == 'X' or winner == 'O':
        print(winner + ' выиграл')
    elif winner == None:
        print('ничья')

def hod(player):
    print('ход ' + player)
    position = input('ход от 1 до 9:')

    valid = False
    while not valid:
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Ошибка - ход от 1 до 9:')

        position = int(position) - 1

        if pole[position] == '-':
            valid = True
        else:
            print('занято')

    pole[position] = player
    doska()

def gameover():
    if_win()
    if_tie()

def if_win():
    global winner
    rows_win = rows()
    columns_win = columns()
    diagonals_win = diagonals()
    if rows_win:
        winner = rows_win
    elif columns_win:
        winner = columns_win
    elif diagonals_win:
        winner = diagonals_win
    else:
        winner = None
    return

def rows():
    global igra
    row_1 = pole[0] == pole[1] == pole[2] != '-'
    row_2 = pole[3] == pole[4] == pole[5] != '-'
    row_3 = pole[6] == pole[7] == pole[8] != '-'
    if row_1 or row_2 or row_3:
        igra = False
    if row_1:
        return pole[0]
    elif row_2:
        return pole[3]
    elif row_3:
        return pole[6]
    return

def columns():
    global igra
    columns_1 = pole[0] == pole[3] == pole[6] != '-'
    columns_2 = pole[1] == pole[4] == pole[7] != '-'
    columns_3 = pole[2] == pole[5] == pole[8] != '-'
    if columns_1 or columns_2 or columns_3:
        igra = False
    if columns_1:
        return pole[0]
    elif columns_2:
        return pole[1]
    elif columns_3:
        return pole[2]
    return

def diagonals():
    global igra
    diagonals_1 = pole[0] == pole[4] == pole[8] != '-'
    diagonals_2 = pole[6] == pole[4] == pole[2] != '-'
    if diagonals_1 or diagonals_2:
        igra = False
    if diagonals_1:
        return pole[0]
    elif diagonals_2:
        return pole[6]
    return

def if_tie():
    global igra
    if '-' not in pole:
        igra = False
    return

def turn():
    global player
    if player == 'X':
        player = 'O'
    elif player == 'O':
        player = 'X'
    return

play()