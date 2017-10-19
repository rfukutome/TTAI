from board import Board, X, O, BLANK

if __name__ == "__main__": 
    game_board = Board()
    game_board.set_board_position(0, 2, O)
    game_board.set_board_position(1, 1, X)
    game_board.set_board_position(2, 0, X)
    print(game_board)