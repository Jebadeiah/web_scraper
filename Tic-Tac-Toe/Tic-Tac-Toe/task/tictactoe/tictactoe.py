board = ['   ', '   ', '   ']
game_round = 0
win = False


def game_win(g_board, var):
    if (g_board[0] == var or g_board[1] == var or g_board[2] == var
            or g_board[0][0] + g_board[1][0] + g_board[2][0] == var
            or g_board[0][1] + g_board[1][1] + g_board[2][1] == var
            or g_board[0][2] + g_board[1][2] + g_board[2][2] == var
            or g_board[0][0] + g_board[1][1] + g_board[2][2] == var
            or g_board[0][2] + g_board[1][1] + g_board[2][0] == var):
        return True


def check_game(g_board):
    global win
    if not game_win(g_board, 'XXX') and not game_win(g_board, 'OOO') and ' ' not in ''.join(g_board):
        print('Draw')
        win = True
    elif game_win(g_board, 'XXX'):
        print("X wins")
        win = True
    elif game_win(g_board, 'OOO'):
        print("O wins")
        win = True


while True:
    game_round += 1
    print("""
    ---------
    | {} {} {} |
    | {} {} {} |
    | {} {} {} |
    ---------
    """.format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1],
               board[1][2], board[2][0], board[2][1], board[2][2]))
    check_game(board)
    if win:
        break
    while True:
        print("Enter the coordinates: ")
        play = input().split()
        if int(play[0]) not in range(0, 4) or int(play[1]) not in range(0, 4):
            print("Coordinates should be from 1 to 3!")
        else:
            game_list = list(board[int(play[0]) - 1])
            if not int(play[0]) or not int(play[1]):
                print("You should enter numbers!")
            elif game_list[int(play[1])-1] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                if game_round % 2 == 1:
                    game_list[int(play[1]) - 1] = 'X'
                else:
                    game_list[int(play[1]) - 1] = 'O'
            board[int(play[0]) - 1] = ''.join(game_list)
        break
