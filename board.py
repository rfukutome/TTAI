from random import randint

X = ' X '
O = ' O '
BLANK = '   '
CATS_GAME = 'CG'
MAX_NUMBER_OF_TURNS = 9
MIN_MOVES_FOR_WIN = 5

class Board():
    def __init__(self):
        self.__board = [[BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK]]
        self.__number_of_turns = 0
        self.__player_turn = [X, O][randint(0, 1)]

    def __str__(self):
        board_string = ""
        for row in self.__board:
            board_string += "------------\n"
            board_string += '|'.join(row) + "\n"
        board_string += "------------\n"
        return board_string

    def set_board_position(self, row, column):
        '''
        Set player token on board position
        @param str player: X or O - which player to set
        @param int row: which row to set
        @param int column: which column to set
        @return: None
        @rtype: None
        '''
        if self.__board[row][column] != BLANK:
            print('Board Position already taken, please choose valid position')
            return False
        self.__board[row][column] = self.__player_turn
        print('IN SET BOARDPOSITION %s' % self.__player_turn)
        self.__player_turn = X if self.__player_turn == O else O
        self.__number_of_turns += 1
        return True

    def reset_board(self):
        '''
        Resets the board for a new round of tic tac toe
        @return: None
        @rtype: None
        '''
        self.__board = [[BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK]]
        self.__number_of_turns = 0
        self.__player_turn = [X, O][randint(0, 1)]

    def determine_win(self):
        '''
        Determine if a player has won.
        @return: None
        @rtype: None
        '''
        if self.__number_of_turns < MIN_MOVES_FOR_WIN:
            return BLANK

        for row in self.__board:
            if row[0] != BLANK and row.count(row[0]) == len(row):
                return row[0]

        for column in (zip(*self.__board)):
            if column[0] != BLANK and column.count(column[0]) == len(column):
                return column[0]

        # If middle spot is taken, no other win conditions
        if self.__board[1][1] == BLANK:
            return BLANK

        # Remaining diagonal win conditions
        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2]:
            return self.__board[0][0]

        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0]:
            return self.__board[0][2]

        if self.__number_of_turns == MAX_NUMBER_OF_TURNS:
            return CATS_GAME

        return BLANK

    def get_player_turn(self):
        return self.__player_turn