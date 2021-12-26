# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#CONSIDERONS:

#Current player: donnée
Current_player = 'X'

#Winner: donnée
Winner = False

game_over = False


#------------------------------------------------------------------------------
# Display the game board to the screen


def display_board():
    print(" ")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print(" ")



def flip_player():
    global Current_player
    if Current_player == 'X':
        Current_player = 'O'
    elif Current_player == 'O':
        Current_player = 'X'

#------------------------------------------------------------------------------

#Check game winner

def check_winner():

    # -----------------------------

    def checkrow():

        global Winner

        row_1 = board[0] == board[1] == board[2] != "-"
        row_2 = board[3] == board[4] == board[5] != "-"
        row_3 = board[6] == board[7] == board[8] != "-"

        if row_1 or row_2 or row_3:
            Winner = True

    checkrow()

    # -----------------------------

    def checkcolumns():

        global Winner

        columns_1 = board[0] == board[3] == board[6] != "-"
        columns_2 = board[1] == board[4] == board[7] != "-"
        columns_3 = board[2] == board[5] == board[8] != "-"

        if columns_1 or columns_2 or columns_3:
            Winner = True

    checkcolumns()

    # -----------------------------


    def checkdiagnols():

        global Winner

        diagnol_1 = board[0] == board[4] == board[8] != "-"
        diagnol_2 = board[2] == board[4] == board[6] != "-"

        if diagnol_1 or diagnol_2:
            Winner = True

    checkdiagnols()


def handle_player():
    position = input(f"Fin Baghi t7at {Current_player}, Serbina: ")

    while board[int(position) - 1] != "-" or int(position) not in range(1, 10):
        position = input("Please enter a verified position: ")
    else:
        board[int(position) - 1] = Current_player
        flip_player()

#STEPS
#-----------------------------------------------------------------------------------------


i = 0
limit = 9
while Winner == False:
    display_board()

    handle_player()
    i += 1

    check_winner()

    if i == limit:
        print("There is a Tie about, Play again")
        break

else:
    flip_player()
    display_board()
    print(f'Congartulation, {Current_player} has Won')

#-----------------------------------------------------------------------------------------