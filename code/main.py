import pygame
from Player import Player
from Tile_map import Tiles


SIZE = WIDTH, HEIGHT = 1000, 600
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30
source = '../source/'
tiles_path = f'{source}/tilemap.png'
csv_path = f'{source}/sity._ground.csv'
csv_path_1 = f'{source}/sity._object.csv'
animation_delay = 10
an_frame = 0
map_scale = 2


pygame.init()
pygame.display.set_caption('Pygame')
display = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(64, 64, (110, 120))
all_sprites.add(player)

map_ground = Tiles(tiles_path, csv_path, (1, 1), (16, 16), False, map_scale)
map_object = Tiles(tiles_path, csv_path_1, (1, 1), (16, 16), False, map_scale)
map_ground.load_tiles()
map_object.load_tiles()


running = True
while running:
    clock.tick(FPS)
    an_frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((50, 50, 50))

    display.blit(map_ground.tiles[0], (0, 0))
    map_ground.draw_map(display)
    map_object.draw_map(display)

    all_sprites.update(display, an_frame, animation_delay)
    all_sprites.draw(display)

    pygame.display.update()
    if an_frame >= animation_delay:
        an_frame = 0
pygame.quit()
