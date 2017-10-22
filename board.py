from random import randint

X = ' X '
O = ' O '
BLANK = '   '

MIN_MOVES_FOR_WIN = 5

class Board():
    def __init__(self):
        self.__board = [[BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK]]
        self.__player_turn = BLANK
        self.__number_of_turns = 0

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
            return False
        self.__board[row][column] = self.__player_turn
        self.__player_turn = [X, O][self.__player_turn == O]
        print('IN SET BOARDPOSITION %s' % self.__player_turn)
        self.__number_of_turns += 1
        self.determine_win()
        return True

    def reset_board(self):
        print("RESTARTING BOARD")
        self.__board = [[BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK],
                        [BLANK, BLANK, BLANK]]
        self.__number_of_turns = 0
        self.__player_turn = [X, O][randint(0, 1)]
        print("Players turn is now %s" % self.__player_turn)

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
        if self.__game_board[0][0] == self.__game_board[1][1] == self.__game_board[2][2]:
            return self.__game_board[0][0]

        if self.__game_board[0][2] == self.__game_board[1][1] == self.__game_board[2][0]:
            return self.__game_board[0][2]

        return BLANK
