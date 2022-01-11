def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

board = create_board()
print(board)

#i just made a change