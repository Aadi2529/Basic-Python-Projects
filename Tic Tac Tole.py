# STEP 1

def display_board(board):
   
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)


# STEP2

def player_input():

    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''

    marker= ' '

    while marker != 'X' and marker !='O':
      marker = input("Player 1:Do you want to be X or O ").upper()


    if marker == 'X':
        return ('X','O')
    else :
        return ('O', 'X')

# Player1_marker , Player2_marker = player_input()
# print(f"Player 1: {Player1_marker}, Player 2: {Player2_marker}")


# STEP 3

def place_marker(board, marker, position):
    board[position] = marker


# STEP 4
 
def win_check(board,mark):

    # WIN TIC TAC TOE?

    # ALL ROWS, and check to see if they are all share the same marker
    # ALL COLUMNS, and check to see if marker matches
    # 2 diagonals, check to see match

    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


#STEP 5
import random
def choose_flip():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 2'
    else :
        return 'Player 1'
    
# STEP 6
def space_check(board, position):
    return board[position] == ' '



# STEP 7

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# STEP 8

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position= int(input("Choose a position: (1-9)"))

    return position


# STEP 9

def replay():
    
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# STEP 10

# WHILE LOOP TO KEEP RUNNING THE GAME

print("Wlecome to Tic Tac Toe:")

while True:
    # PLAY THE GAME HERE

    # SET EVERYTHING UP (BOARDS, WHOS FRIST,CHOOSE MARKERS X,O)

    the_board = [' ']*10
    Player1_marker, Player2_marker = player_input()

    turn = choose_flip()
    print(turn + " wiil go frist")
    
    play_game = input("Ready to play? y or n? ")

    if play_game == 'y':
        game_on =True

    else :
        game_on = False

    #GAME PLAY

    while game_on:
        if  turn == 'Player 1':
            # SHOW THE BOARD
            display_board(the_board)
            
            # CHOOSE A POSITION
            position = player_choice(the_board)
            # PLACE THE MARKER ON THE POSITION
            place_marker(the_board, Player1_marker, position)

            # CHECK IF THEY WON
            if win_check(the_board, Player1_marker):
                display_board(the_board)
                print("PLAYER 1 HAS WON!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = 'Player 2'
            # PLAYER 1 TURN
        else:
            # SHOW THE BOARD
            display_board(the_board)
            
            # CHOOSE A POSITION
            position = player_choice(the_board)
            # PLACE THE MARKER ON THE POSITION
            place_marker(the_board, Player2_marker, position)

            # CHECK IF THEY WON
            if win_check(the_board, Player1_marker):
                display_board(the_board)
                print("PLAYER 2 HAS WON!!!")
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!!!")
                    game_on = False
                else:
                    turn = 'Player 1'
        






    if not replay():
        break
# BREAK OUT THE WHILE LOOP ON replay()