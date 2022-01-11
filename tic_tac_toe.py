#Tic-Tac-Toe game 

# tasks that i need my program to do:

# create a board
# display a board 

# prompt the user for their choice
# switch users after each turn

# update the board with the users choice

# check to see if the user has won after the fifth turn up to the 9th turn
# check to see if there is a tie on the 9th turn

# end the game after on the 1oth turn
# display who the winner is
def main():
    board = create_board()
    display_board(board)
    player = "X"
    choice = get_choice(player)
    print(choice)

def create_board():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board

def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")

def get_choice(player):
    choice = int(input(f"{player}'s turn to choose a square (1-9): "))
    return choice

if __name__ == "__main__":
    main()
