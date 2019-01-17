from IPython.display import clear_output
import random

def choose_first():
    return random.randint(1,2)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Please enter if Player 1 wants to choose X or O?')
    player1 = marker
    if player1 == 'X':        
        player2 = 'O'        
    else:    
        player2 = 'X'
    return (player1, player2)

def display_board(inpt):
    clear_output()
    print(' {} | {} | {} '.format(inpt[0],inpt[1],inpt[2]))
    print('------------')
    print(' {} | {} | {} '.format(inpt[3],inpt[4],inpt[5]))
    print('------------')
    print(' {} | {} | {} '.format(inpt[6],inpt[7],inpt[8]))

def set_marker(board, marker, pos):
    if(pos < 9):
        board[pos] = marker
    return board

def check_win(board, mark):
    win = False
    if board[0] == board[1] == board[2] == mark:
        win= True
    elif board[3] == board[4] == board[5] == mark:
        win = True
    elif board[6] == board[7] == board[8] == mark:
        win = True
    elif board[0] == board[3] == board[6] == mark:
        win = True
    elif board[1] == board[4] == board[7] == mark:
        win = True
    elif board[2] == board[5] == board[8] == mark:
        win = True
    elif board[6] == board[7] == board[8] == mark:
        win = True
    elif board[0] == board[4] == board[8] == mark:
        win = True
    elif board[6] == board[4] == board[2] == mark:
        win = True
    return win

def space_check(board,pos):
    return board[pos] == ' '

def full_board(board):
    full = True
    for box in board:
        if box == ' ':
            full = False
            break
    return full

def player_choice(player):
    return int(input('Please enter the next position for {}: '.format(player)))


def replay():
    return bool(input('Would you like to play again: ').lower() == 'yes')

game_board = [' '] * 9
gameovr = False
isFull = False
current_marker = 1

(player1_marker,player2_marker) = player_input()
display_board(game_board)

first_player = choose_first()
if first_player == 1:
    current_marker = player1_marker
    print('Player 1 will play first.')
else:
    current_marker = player2_marker
    print('Player 2 will play first.')

while (not gameovr and not isFull):
    position = player_choice(current_marker)
    if space_check(game_board,position):        
        game_board = set_marker(game_board, current_marker, position)
        display_board(game_board)
        gameovr = check_win(game_board, current_marker)
        isFull = full_board(game_board)

        if isFull:
            print('Game ended in a tie')
            if replay():
                gameovr = False
                isFull = False
                game_board = [' '] * 9
            else:
                print('Thank you for playing.')
        if gameovr:
            if current_marker == player1_marker:
                print('Player 1 has won the game.')
            elif current_marker == player2_marker:
                print('Player 2 has won the game')
            if replay():
                gameovr = False
                isFull = False
                game_board = [' '] * 9
            else:
                print('Thank you for playing.')

        if current_marker == player1_marker:
            current_marker = player2_marker
        else :
            current_marker = player1_marker
    # playermove = int(input('Enter the position you want to fill: '))
    # if playerorder == 0:
    #     arr[playermove] = 'X'
    #     playerorder = 1
    # elif playerorder == 1:
    #     arr[playermove] = 'O'
    #     playerorder = 0
    # display_board(arr)
    # count += 1
    # print(count)