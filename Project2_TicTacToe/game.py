dataset = ['', '', '', '', '', '', '', '', '']

def game_rules():
    print('=' * 40)
    print('Welcome to Tic Tac Toe')
    print('''GAME RULES:
    Each player can place one mark (or stone) per turn on the 3x3 grid
    The WINNER is who succeeds in placing three of their marks in a
    * horizontal,
    * vertical or
    * diagonal row
    ''')
    print("Let's start the game")


def show_board(my_list):
    N = 3
    print('=' * 10)
    print(f'\n'.join([' |'.join(i) for i in zip(*[iter(my_list)] * N)]))
    print('=' * 10)

def ask_for_move(turn):
    if turn % 2 == 0:
        char = 'O'
        while True:
            try:
                index = int(input(f'Player {char} | Please enter your move number: '))
            except ValueError:
                print('Wrong input')
                continue
            else:
                return index, char
                break
    if turn % 2 == 1:
        char = 'X'
        while True:
            try:
                index = int(input(f'Player {char} | Please enter your move number: '))
            except ValueError:
                print('Wrong input')
                continue
            else:
                return index, char
                break
def move(index, char):
    index = int(index)
    dataset[index-1] = char

def check_move(index):
    if dataset[index-1] != '':
        return False
    else:
        return True
def check_board(board):
    if not '' in board:
        print('No more moves possible. Game has no winner. GAME OVER')
        exit()
def check_winner(board):
    if ((board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or
            (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or
            (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or
            (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or
            (board[2] == 'X' and board[4] == 'X' and board[6] == 'X') or
            (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or
            (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or
            (board[2] == 'X' and board[5] == 'X' and board[8] == 'X')):
        return True
    if ((board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or
            (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or
            (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or
            (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or
            (board[2] == 'O' and board[4] == 'O' and board[6] == 'O') or
            (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or
            (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or
            (board[2] == 'O' and board[5] == 'O' and board[8] == 'O')):
        return True
    else:
        return False


def main():
    game_rules()
    turn = 0
    while True:
        check_board(dataset)
        index, char = ask_for_move(turn)
        if check_move(index) == False:
            print('This field is occupied. Please select another one.')
            continue
        else:
            move(index, char)
            show_board(dataset)
            turn += 1
        if check_winner(dataset) == True:
            print('CONGRATULATIONS. Winner is player', char)
            break

main()