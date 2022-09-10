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

        map_pos_w, map_pos_h = WIDTH // 8, HALF_HEIGHT // 2
        map_size_w, map_size_h = HEIGHT // 4, WIDTH / 4
        tile_size_w, tile_size_h = map_size_w // MAP_HEIGHT, map_size_h // MAP_WIDTH

        pg.draw.rect(self.game.screen, 'black', (map_pos_w, map_pos_h, map_size_w, map_size_h))

        [pg.draw.rect(self.game.screen, 'darkgray', (
            pos[1] * tile_size_w + map_pos_w,
            - pos[0] * tile_size_h + map_pos_w + map_size_h,
            tile_size_w, tile_size_h))
         for pos in self.world_map]

        pg.draw.rect(self.game.screen, 'blue',
                     (map_pos_w + tile_size_w, map_pos_h + map_size_h - 2 * tile_size_h, tile_size_w, tile_size_h))

        print(self.world_map)
