from board import Board, X, O, BLANK
#from board_gui import BoardGui

import tkinter


if __name__ == "__main__":
    game_board = Board()
    gui_board = tkinter.Tk()
    gui_board.title("       TTAI")
    gui_board.geometry("400x400")
    gui_board.wm_iconbitmap("ttai.ico")

    photo = tkinter.PhotoImage(file="blank.gif")
    restart_game_button = tkinter.Button(gui_board, text ="Restart", command = game_board.reset_board)
    #game_start_button = tkinter.Button(gui_board, text = "Game Start")

    top_left_button = tkinter.Button(gui_board, text = "Top Left", command = lambda:game_board.set_board_position(0, 0))
    top_middle_buttom = tkinter.Button(gui_board, width = 15, height = 7, text = "Top Middle", command = lambda:game_board.set_board_position(0, 1))
    top_right_button = tkinter.Button(gui_board, width = 15, height = 7, text = "Top Right", command = lambda:game_board.set_board_position(0, 2))

    left_button = tkinter.Button(gui_board, width = 15, height = 7, text = "Left", command = lambda:game_board.set_board_position(1, 0))
    middle_button = tkinter.Button(gui_board, width = 15, height = 7, text = "Middle", command = lambda:game_board.set_board_position(1, 1))
    right_button = tkinter.Button(gui_board, width = 15, height = 7, text = "Right", command = lambda:game_board.set_board_position(1, 2))

    bottom_left_button = tkinter.Button(gui_board, width = 15, height = 7, text = "Bottom Left", command = lambda:game_board.set_board_position(2, 0))
    bottom_middle_buttom = tkinter.Button(gui_board, width = 15, height = 7, text = "Bottom Middle", command = lambda:game_board.set_board_position(2, 1))
    bottom_right_button = tkinter.Button(gui_board, width = 15, height = 7, text = "Bottom Right", command = lambda:game_board.set_board_position(2, 2))    


    top_left_button.grid(column=0, row=0)
    top_left_button.config(image=photo, height="100", width="100")
    top_middle_buttom.grid(column=1, row=0)
    top_right_button.grid(column=2, row=0)
    left_button.grid(row=2, column=0)
    middle_button.grid(row=2, column=1)
    right_button.grid(row=2, column=2)
    bottom_left_button.grid(row=3, column=0)
    bottom_middle_buttom.grid(row=3, column=1)
    bottom_right_button.grid(row=3, column=2)
    restart_game_button.grid(columnspan=3)
    gui_board.mainloop()

    print(game_board)