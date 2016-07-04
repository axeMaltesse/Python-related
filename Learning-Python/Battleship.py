#importing randint
from random import randint

#creating an empty list
board = []

#filling up the list by O and creating a two dimensionall array
for x in range(5):
    board.append(["O"] * 5)

#printing function which also includes a spaces to show clear grid
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

#random functions to generate a ship; Can be also a for loop if you want more than 1 ship
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

#remembering the ship 
ship_row = random_row(board)
ship_col = random_col(board)

#game loop
for turn in range(4):
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            if(turn == 3):
                print "Game Over"
        print (turn+1)
        print_board(board)
