import pygame as pg
import sys
from settings import *
from map import *

BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)  # why RES?
        self.clock = pg.time.Clock()
        # self.running = True
        # self.state = 'start'
        # self.load_data()
        self.new_game()

    # def load_data(self):
    #     pass

    def new_game(self):
       self.map = Map(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps():.1f}')

    def draw(self):
        self.screen.fill(BLACK)
        self.map.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # self.running = False
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    # self.running = False
                    pg.quit()
                    sys.exit()
                # if event.key == pg.K_SPACE:
                #     self.new_game()
                #     self.state = 'playing'
            # if event.type == pg.KEYUP:
            #     if event.key == pg.K_SPACE:
            #         self.state = 'start'

    def run(self):
        while True: #self.running:
            self.check_events()
            self.update()
            self.draw()

            # if self.state == 'start':
            #     self.draw()
            # if self.state == 'playing':
            #     self.update()
            # if self.state == 'game over':
            #     self.draw()
            # if self.state == 'you win':
            #     self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
