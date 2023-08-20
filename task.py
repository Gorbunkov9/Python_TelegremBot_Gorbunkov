from colorama import Fore, Back, Style


def draw_board(board):  # функция выводящая на экран карту игры
    for i in board:
        print('———————')
        print('|', end='')
        for j in i:
            if j == 'X':
                print(Fore.RED + 'X' + Style.RESET_ALL + '|', end='')
            elif j == 'O':
                print(Fore.GREEN + 'O' + Style.RESET_ALL + '|', end='')
            elif j == ' ':
                print(Back. YELLOW + ' ' + Style.RESET_ALL + '|', end='')
        print()
    print('———————')


def ask_move(symbol, board):  # функция проверяющая свободна ли ячейка и выводящая координаты для хода
    while True:
        x = input('Введите координату X нужной ячейки ')
        if x not in ['1', '2', '3']:
            print('Проверьте правильность координаты: она должна быть от 1 до 3')
            continue
        else:
            x = int(x)
            break

    while True:
        y = input('Введите координату Y нужной ячейки ')
        if y not in ['1', '2', '3']:
            print('Проверьте правильность координаты: она должна быть от 1 до 3')
            continue
        else:
            y = int(y)
            break

    if board[x-1][y-1] == ' ':
        return x, y
    else:
        print('Ячейка занята')
        ask_move(symbol, board)


def make_move(symbol, board, x, y):  # функция делающая ход
    board[x-1][y-1] = symbol
    return draw_board(board)


def ask_and_make_move(symbol, board):  # функция объединяющая выбор ячейки, проверку пустоты ячейки и постановку символа
    x, y = ask_move(symbol, board)
    make_move(symbol, board, x, y)
    check_win(symbol, board)

def check_win(symbol, board):
    for i in range(3):
        # проверка по горизонтали
        if board[i] == [symbol, symbol, symbol]:
            return True
        # проверка по вертикали
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
        # проверка по диагонали слева направо
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    # проверка по диагонали справа налево
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True
    return False


def tic_tac_toe():
    while True:  # бесконечный цикл проводящий игры
        symbol = 'X'
        board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        while True:  # бесконечный цикл конкретной игры
            draw_board(board)  # рисуем игровое поле
            ask_and_make_move(symbol, board)  # даем возможность выбрать место и сделать ход
            if check_win(symbol, board):  # проверка на победу
                print(f'Игрок {symbol} выиграл!')
                break
            tie_flag = False  # проверка на ничью
            for i in board:
                for j in i:
                    if j == ' ':
                        tie_flag = True
            if tie_flag == False:
                print('Ничья')
                break
            symbol = "O" if symbol == "X" else "X"
        restart = input('Сыграем еще? (Да/Нет) ')
        if restart.lower() == 'нет':
            break


tic_tac_toe()