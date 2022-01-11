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
    turn = 0
    player = switch_player(turn)
    board = create_board()
    display_board(board)
    choice = get_choice(player)
    print(choice)

    turn += 1

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

def switch_player(turn):
    if (turn % 2) == 0:
        player = "X"    
    else: 
        player = "O"
    return player

def updated_board(board, choice, player):
    index = choice -1
    board[index] = player
    return board

def check_for_win(board, player):
    win = False
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or 
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):
        win = True
        print(f"Player {player} wins!")
        return win
    else:
        win = False
        return 
        
def check_for_tie(win, turn):
    if turn == 9 and win == False:
        print("The game is a tie")


if __name__ == "__main__":
    main()
