from board import Board, X, O, BLANK
import tkinter


if __name__ == "__main__":
    game_board = Board()
    gui_board = tkinter.Tk()
    restart_game_button = tkinter.Button(gui_board, text ="Restart", command = game_board.reset_board())
    #game_start_button = tkinter.Button(gui_board, text = "Game Start")
    top_left_button = tkinter.Button(gui_board, text = "Top Left", command = game_board.set_board_position(0, 0))
    top_middle_buttom = tkinter.Button(gui_board, text = "Top Middle", command = game_board.set_board_position(0, 1))
    top_right_button = tkinter.Button(gui_board, text = "Top Right", command = game_board.set_board_position(0, 2))

    left_button = tkinter.Button(gui_board, text = "Left", command = game_board.set_board_position(1, 0))
    middle_button = tkinter.Button(gui_board, text = "Middle", command = game_board.set_board_position(1, 1))
    right_button = tkinter.Button(gui_board, text = "Right", command = game_board.set_board_position(1, 2))

    bottom_left_button = tkinter.Button(gui_board, text = "Bottom Left", command = game_board.set_board_position(2, 0))
    bottom_middle_buttom = tkinter.Button(gui_board, text = "Bottom Middle", command = game_board.set_board_position(2, 1))
    bottom_right_button = tkinter.Button(gui_board, text = "Bottom Right", command = game_board.set_board_position(2, 2))    

    top_left_button.pack()
    top_middle_buttom.pack()
    top_right_button.pack()
    left_button.pack()
    middle_button.pack()
    right_button.pack()
    bottom_left_button.pack()
    bottom_middle_buttom.pack()
    bottom_right_button.pack()
    restart_game_button.pack()
    gui_board.mainloop()


    print(game_board)