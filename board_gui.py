import tkinter
from board import Board

class BoardGui():
	def __init__(self):
	    self.__gui_board = tkinter.Tk()
	    self.__gui_board.title("       TTAI")
	    self.__gui_board.geometry("400x400")
	    self.__gui_board.wm_iconbitmap("ttai.ico")
	    self.__board = Board()

	    photo = tkinter.PhotoImage(file="blank.gif")
	    restart_game_button = tkinter.Button(self.__gui_board, text ="Restart", command = self.__board.reset_board)
	    #game_start_button = tkinter.Button(gui_board, text = "Game Start")

	    top_left_button = tkinter.Button(self.__gui_board, text = "Top Left", command = lambda:self.__board.set_board_position(0, 0))
	    top_middle_buttom = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Top Middle", command = lambda:self.__board.set_board_position(0, 1))
	    top_right_button = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Top Right", command = lambda:self.__board.set_board_position(0, 2))

	    left_button = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Left", command = lambda:self.__board.set_board_position(1, 0))
	    middle_button = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Middle", command = lambda:self.__board.set_board_position(1, 1))
	    right_button = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Right", command = lambda:self.__board.set_board_position(1, 2))

	    bottom_left_button = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Bottom Left", command = lambda:self.__board.set_board_position(2, 0))
	    bottom_middle_buttom = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Bottom Middle", command = lambda:self.__board.set_board_position(2, 1))
	    bottom_right_button = tkinter.Button(self.__gui_board, width = 15, height = 7, text = "Bottom Right", command = lambda:self.__board.set_board_position(2, 2))

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
	    self.__gui_board.mainloop()