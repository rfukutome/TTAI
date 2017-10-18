from pip._vendor.distlib.compat import raw_input

X     = '  X  '
O     = '  O  '
BLANK = '     '
MINIMUM_MOVES_TO_WIN = 4


class GameBoard:
    def __init__(self):
        self.__number_of_moves = 0
        self.__game_board  = [[BLANK, BLANK, BLANK],
                            [BLANK, BLANK, BLANK],
                            [BLANK, BLANK, BLANK]]

    def __str__(self):
        '''
        Gets a human readable tic tac toe board
        @return: tic tac toe board
        @rtype: str
        '''
        game_board_string = '+-----------------+\n'
        for row in self.__game_board:
            game_board_string += '|' + '|'.join(row) + '|' + '\n+-----------------+\n'
        return game_board_string
    
    def set_square(self, player, row, column):
        '''
        Sets a square on the game board
        @param player: X or O - which player to set
        @type player: str
        @param row: which row to set
        @type row: int
        @param column: which column to set
        @type column: int
        @return: None
        @rtype: None
        '''
        if player not in (X, O):
            print('invalid move')
            return  # TODO: handle

        # TODO: validate row and column (int type)
        if int(row) > 3 or int(column) > 3:
            print('invalid move')
            return

        if self.__game_board[int(column)][int(row)] != BLANK:
            print('invalid move')
            return

        self.__game_board[int(column)][int(row)] = player
        self.__number_of_moves += 1

    def NumberOfMoves(self):
        '''
        Getter for the number of moves that have been played
        @return: Number of moves played
        @rtype: int

        '''
        return self.__number_of_moves

    def win_condition(self):
        '''
        Check if someone has won
        @return: True is someone has won
        @rtype: bool
        '''
        if self.__number_of_moves < MINIMUM_MOVES_TO_WIN:
            return False

        for row in self.__game_board:
            if row[0] != BLANK and row.count(row[0]) == len(row):
                return True

        for column in (zip(*self.__game_board)):
            if column[0] != BLANK and column.count(column[0]) == len(column):
                return True

        # Middle spot must be occupied for diagonal
        if self.__game_board[1][1] == BLANK:
            return False

        # TODO: brute force is bad ok... fix it
        if self.__game_board[0][0] == self.__game_board[1][1] == self.__game_board[2][2]:
            return True

        if self.__game_board[0][2] == self.__game_board[1][1] == self.__game_board[2][0]:
            return True

        return False


if __name__ == '__main__':

    game_board = GameBoard()

    print('LETS PLAY!')

    player = None
    number_of_plays = 0

    while not game_board.win_condition():

        player = [X, O][number_of_plays % 2]
        
        row = raw_input('%s, Pick your row (0-2): ' % player)
        column = raw_input('%s, Pick column (0-2): ' % player)
        
        game_board.set_square(player, row, column)
        number_of_plays += 1
        print('%s' % game_board.__str__())

    print ('WINNER WINNER %s' % player)
