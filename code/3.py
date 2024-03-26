import csv
import pygame
import os

SIZE = WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (255, 255, 255)
FPS = 24

tile_file = '../source/tmw_desert_spacing.png'
csv_file = '../source/desert.csv'


class Tiles(pygame.sprite.Sprite):
    def __init__(self, file_path, size=(32, 32)):
        super().__init__()
        self.tiles = []
        self.tiles_map = pygame.sprite.Group()
        self.map_size = (0, 0)
        self.size = size
        self.image = pygame.image.load(file_path)
        self.max_size = self.image.get_size()
        self.tile = pygame.Surface(self.size)

    def load_tiles(self):
        for y in range(1, self.max_size[1], self.size[1]+1):
            for x in range(1, self.max_size[0], self.size[0]+1):
                self.tile = pygame.Surface(self.size)
                self.tile.blit(self.image, (0, 0), (x, y, self.size[0], self.size[1]))
                self.tiles.append(self.tile)

    def draw_tilemap(self, display, csv_file):
        with open(csv_file, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            x = 0
            y = 0
            for row in read:
                x = 0
                for tile in row:
                    display.blit(self.tiles[int(tile)], (x, y))
                    x += self.size[0]
                y += self.size[1]
            self.map_size = (x * self.size[0], y * self.size[1])
        return self.map_size

    def get_map_size(self):
        with open(csv_file, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            x = 0
            y = 0
            for row in read:
                x = 0
                for tile in row:
                    x += self.size[0]
                y += self.size[1]
            self.map_size = (x, y)
        return self.map_size


pygame.init()


map = Tiles(tile_file)
map.load_tiles()


display = pygame.display.set_mode(map.get_map_size())
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill(BACKGROUND_COLOR)

    map.draw_tilemap(display, csv_file)

    pygame.display.update()

pygame.quit()
