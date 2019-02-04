

class Board():

    def __init__(self):

        self.board = self.new_board();

    def new_board(self):

        """
        create a new board

        :return: The board to be ues in the init
        """

        # initialize the board squres (black or white)

        board = [[None] * 8 for i in range(8)]

        for y in range(8):
            for x in range(8):
                if (x % 2 != 0) and (y % 2 == 0):
                    board[y][x] = "White"
                elif (x % 2 == 0) and (y % 2 != 0):
                    board[y][x] = "Black"
                elif (x % 2 != 0) and (y % 2 != 0):
                    board[y][x] = "White"
                elif (x % 2 == 0) and (y % 2 == 0):
                    board[y][x] = "Black"

        print(board)
