import pygame as pg

from settings import *

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 3, 3, 3, 3, _, _, _, 2, 2, 2, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, 1, 3, 1, 3, 1, 1, 4, 4, _, 4, 4, 1, 1, 1]
]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):  # test method, only mesh of the map

        pg.draw.rect(self.game.screen, 'black', (MAP_POS_W, MAP_POS_H, MAP_SIZE_W, MAP_SIZE_H))

        for pos in self.world_map:
            x, y = pos
            w = y * TILE_MAP_W + MAP_POS_W
            h = - x * TILE_MAP_H + MAP_POS_H + MAP_SIZE_H - TILE_MAP_H

            pg.draw.rect(self.game.screen, 'darkgray', (w, h, TILE_MAP_W, TILE_MAP_H))

        pg.draw.rect(self.game.screen, 'blue',
                     (MAP_POS_W + TILE_MAP_W, MAP_POS_H + MAP_SIZE_H - 2 * TILE_MAP_H, TILE_MAP_W, TILE_MAP_H))
