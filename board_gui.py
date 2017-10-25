import tkinter

from tkinter import *
from board import Board, X, O, BLANK, CATS_GAME

class BoardGui():
    def __init__(self):
        self.__gui_board = tkinter.Tk()
        self.__gui_board.title("       TTAI")
        self.__gui_board.geometry("325x400")
        self.__gui_board.wm_iconbitmap("ttai.ico")
        self.__board = Board()
        self.__tile_list = []
        self.__blank_photo = tkinter.PhotoImage(file="blank.gif")
        self.__x_photo = tkinter.PhotoImage(file="x.gif")
        self.__o_photo = tkinter.PhotoImage(file="circle.gif")
        self.__board_canvas = Canvas(self.__gui_board, height=300, width=300)
        self.__board_canvas.place(relx=0.5, rely=0.5, anchor="center")
        restart_game_button = tkinter.Button(self.__gui_board, text="Restart", command=self.clear_board)

        # Place all buttons on canvas and set command
        top_left_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(0, 0))
        top_middle_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(0, 1))
        top_right_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(0, 2))
        left_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(1, 0))
        middle_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(1, 1))
        right_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(1, 2))
        bottom_left_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(2, 0))
        bottom_middle_buttom = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(2, 1))
        bottom_right_button = tkinter.Button(self.__board_canvas, command=lambda: self.set_tile_element(2, 2))

        # Set position of each of the squares in the grid.
        top_left_button.grid(column=0, row=0)
        top_middle_button.grid(column=1, row=0)
        top_right_button.grid(column=2, row=0)
        left_button.grid(row=2, column=0)
        middle_button.grid(row=2, column=1)
        right_button.grid(row=2, column=2)
        bottom_left_button.grid(row=3, column=0)
        bottom_middle_buttom.grid(row=3, column=1)
        bottom_right_button.grid(row=3, column=2)
        restart_game_button.grid(columnspan=3)

        # Append all buttons to list to be able to iterate through them easily.
        self.__tile_list.append(top_left_button)
        self.__tile_list.append(top_middle_button)
        self.__tile_list.append(top_right_button)
        self.__tile_list.append(left_button)
        self.__tile_list.append(middle_button)
        self.__tile_list.append(right_button)
        self.__tile_list.append(bottom_left_button)
        self.__tile_list.append(bottom_middle_buttom)
        self.__tile_list.append(bottom_right_button)

        self.clear_board()
        self.__gui_board.mainloop()

    def set_tile_element(self, row, column):
        if(self.__board.set_board_position(row, column)):
            square_photo = self.__x_photo if self.__board.get_player_turn() == X else self.__o_photo
            self.__tile_list[row * 3 + column].config(image=square_photo, height="100", width="100")
            winner_string = self.__board.determine_win()
            if winner_string != BLANK and winner_string != CATS_GAME:
                print("WINNER!!")
                self.clear_board()
            elif winner_string == CATS_GAME:
                print("CATS GAME")
                self.clear_board()

    def clear_board(self):
        self.__board.reset_board()
        # Set all squares to a blank tile.
        for square in self.__tile_list:
            square.config(image=self.__blank_photo, height="100", width="100")
