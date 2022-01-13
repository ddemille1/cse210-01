#Tic-Tac-Toe game 
#CSE 210 week 2 Assignment
#Doug DeMille

def main():
    win = False
    tie = False
    turn = 0
    board = create_board()
    display_board(board)
    while win == False and tie == False:
        player = switch_player(turn)
        choice = int(get_choice(player, board))
        updated_board(board, choice, player)
        display_board(board)
        win = check_for_win(board, player)
        tie = check_for_tie(win, turn)
        turn += 1

def create_board():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board

def display_board(board):
    print('')
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print('')

def get_choice(player, board):
    choice = int(input(f"{player}'s turn to choose a square (1-9): "))
    available = check_available(board, choice)
    if available == True:
        return choice
    elif available == False:
        choice = get_choice(player, board)
        return choice
        

def check_available(board, choice):
    available = True
    index = choice -1
    position = board[index]
    if position == "X" or position == "O":
        print("That square is taken. Please choose another square")
        available = False
        return available
    else:
        available = True
        return available



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
        return win
        
def check_for_tie(win, turn):
    if turn == 8 and win == False:
        print("The game is a tie")
        tie = True
        return tie
    tie = False
    return tie

if __name__ == "__main__":
    main()
