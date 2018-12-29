import pygame as pg
from setting import *
import random

class Game:
    def __init__(self):
        # initiallize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game loop - update
        pass


    def events(self):
        # Game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                self.mx, self.my = pg.mouse.get_pos()
                print (self.mx, self.my)


    def draw(self):
        # Game loop - draw
        self.screen.fill((43,123,21))
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 8) , (WIDTH, HEIGHT / 8), 2)
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 8 * 2) , (WIDTH, HEIGHT / 8 * 2), 2)
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 8 * 3) , (WIDTH, HEIGHT / 8 * 3), 2)
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 8 * 4) , (WIDTH, HEIGHT / 8 * 4), 2)
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 8 * 5) , (WIDTH, HEIGHT / 8 * 5), 2)
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 8 * 6) , (WIDTH, HEIGHT / 8 * 6), 2)
        pg.draw.line(self.screen, BLACK, (0, HEIGHT / 8 * 7) , (WIDTH, HEIGHT / 8 * 7), 2)

        pg.draw.line(self.screen, BLACK, (WIDTH / 8, 0) , (WIDTH / 8, HEIGHT), 2)
        pg.draw.line(self.screen, BLACK, (WIDTH / 8 * 2, 0) , (WIDTH / 8 * 2, HEIGHT), 2)
        pg.draw.line(self.screen, BLACK, (WIDTH / 8 * 3, 0) , (WIDTH / 8 * 3, HEIGHT), 2)
        pg.draw.line(self.screen, BLACK, (WIDTH / 8 * 4, 0) , (WIDTH / 8 * 4, HEIGHT), 2)
        pg.draw.line(self.screen, BLACK, (WIDTH / 8 * 5, 0) , (WIDTH / 8 * 5, HEIGHT), 2)
        pg.draw.line(self.screen, BLACK, (WIDTH / 8 * 6, 0) , (WIDTH / 8 * 6, HEIGHT), 2)
        pg.draw.line(self.screen, BLACK, (WIDTH / 8 * 7, 0) , (WIDTH / 8 * 7, HEIGHT), 2)





        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # the start screen
        pass

    def show_go_screen(self):
        # the game-over screen
        pass


    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()