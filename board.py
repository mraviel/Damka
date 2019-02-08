from squre import Squre
from setting import *
import pygame as pg

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

        for x in range(8):
            for y in range(8):
                if (x % 2 != 0) and (y % 2 == 0):
                    board[x][y] = Squre(WHITE, self.squreLocation(x, y))
                elif (x % 2 == 0) and (y % 2 != 0):
                    board[x][y] = Squre(WHITE, self.squreLocation(x, y))
                elif (x % 2 != 0) and (y % 2 != 0):
                    board[x][y] = Squre(BLACK, self.squreLocation(x, y))
                elif (x % 2 == 0) and (y % 2 == 0):
                    board[x][y] = Squre(BLACK, (int(920 / 8 * x + 50),int(920 / 8 * y + 50)))


        print(board)

        return board


    def drawBoardGame(self, screen, board):

        """ Draw the all board on the screen """

        for y in range(8):
            for x in range(8):
                pg.draw.rect(screen, self.board[x][y].color, (WIDTH / 8 * x, HEIGHT / 8 * y, WIDTH / 8, HEIGHT / 8), 0)

        self.drawPiecesOnBoard(screen)


    def drawPiecesOnBoard(self, screen):

        """ Draw the Pieces (players) on the board \ screen """

        # pg.draw.circle(screen, RED, self.board[5][1].pos, 40)

        for x in range(8):
            for y in range(8):
                pass

    def middelSqure(self):

        """ Get the middel of the squre.  Return: tupple of the middel location """

        pass

    def squreLocation(self, x, y):

        """ Get the squre location.  Argumentes: x, y of the location(min(0,0), max(7,7)).
            Return: tupple of the location """

        return (int(920 / 8 * x + 50), int(920 / 8 * y + 50))

