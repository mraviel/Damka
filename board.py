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

        for y in range(8):
            for x in range(8):
                if (x % 2 != 0) and (y % 2 == 0):
                    board[y][x] = Squre(WHITE)
                elif (x % 2 == 0) and (y % 2 != 0):
                    board[y][x] = Squre(WHITE)
                elif (x % 2 != 0) and (y % 2 != 0):
                    board[y][x] = Squre(BLACK)
                elif (x % 2 == 0) and (y % 2 == 0):
                    board[y][x] = Squre(BLACK)


        print(board)

        return board


    def drawBoardGame(self, screen, board):

        for y in range(8):
            for x in range(8):
                pg.draw.rect(screen, self.board[x][y].color, (WIDTH / 8 * x, HEIGHT / 8 * y, WIDTH / 8, HEIGHT / 8), 0)