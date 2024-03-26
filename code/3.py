import csv
import pygame
import os

SIZE = WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (255, 255, 255)
FPS = 24

tile_file = '../source/tmw_desert_spacing.png'
csv_file = '../source/desert.csv'
image = pygame.image.load(tile_file)
rect = image.get_rect()

pygame.init()
display = pygame.display.set_mode(rect.size)
clock = pygame.time.Clock()


class Tiles(pygame.sprite.Sprite):
    def __init__(self, file_path, csv_file, size=(32, 32)):
        super().__init__()
        self.tiles = []
        self.tiles_map = pygame.sprite.Group()
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
        print(self.tiles)

    def draw_tilemap(self):
        with open(csv_file, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            for row in read:
                for tile in row:
                    print(tile)
                    sprite = self.tiles[int(tile)]
                    self.tiles_map.add(sprite)


first = Tiles(tile_file, csv_file)
first.load_tiles()
img = first.tiles
first.draw_tilemap()

all_sprites = pygame.sprite.Group()
all_sprites.add(first.tiles_map)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display.fill(BACKGROUND_COLOR)

    all_sprites.draw(display)

    pygame.display.update()

pygame.quit()
