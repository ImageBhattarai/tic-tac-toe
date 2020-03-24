#------------Global variables-------
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

#If game is still on
game_still_going_on = True

#Who won?
winner = None

#Who's turn is it?
current_player = "X"

def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


def play_game():
    #displays initial board
    display_board()
    
    while game_still_going_on:
        #Handles turn for an individual player
        handle_turn(current_player)
        
        #Checks if game is over
        game_over()
        
        #Switch to the other player
        filp_player()

    #The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner == None:
        print('Tie.')


def game_over():
    check_for_winner()
    check_for_tie()
    
    
def check_for_winner():    
    #Set up global variable
    global winner 
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    #Setting up a global variable
    global game_still_going_on
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #Checking if there is a winner in rows
    if row_1 or row_2 or row_3:
        game_still_going_on = False
    #Checking if X or O is the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #Setting up a global variable
    global game_still_going_on
    #Checking if columns are equal
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    #Checking if there is a winner in columns
    if column_1 or column_2 or column_3:
        game_still_going_on = False
    #Checking if X or O is the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    #Setting up a global variable
    global game_still_going_on
    #Checking if diagonals are equal
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    #Checking if there is a winner in diagonals
    if diagonal_1 or diagonal_2:
        game_still_going_on = False
    #Checking if X or O is the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[3]
    return

def filp_player():
    #Setting up global variable
    global current_player
    # Swaping players
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def check_for_tie():
    global game_still_going_on
    if "-" not in board:
        game_still_going_on = False
    return


def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a number from 1-9: ")
    
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input('Choose a number from 1-9: ')
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("You cannot go there")
    
    board[position] = player
    
    display_board()


play_game()










#board
#display board
#input from player
#win condition
#tie 
#flip players