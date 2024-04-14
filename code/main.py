import pygame
from Player import Player
from Tile_map import Tiles


SIZE = WIDTH, HEIGHT = 1000, 600
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30
an_frame = 0
animation_delay = 10
map_scale = 2

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption('Pygame')
display = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()

source = '../source/'
tiles_path = f'{source}/tilemap.png'
csv_path = f'{source}/sity._ground.csv'
csv_path_1 = f'{source}/sity._object.csv'
collision_objects = f'{source}/collision_map.json'
collision_events = f'{source}/events_objects.json'

all_sprites = pygame.sprite.Group()
player = Player(64, 64, (180, 180))
all_sprites.add(player)

map_ground = Tiles(tiles_path, csv_path, (1, 1), (16, 16), False, map_scale, collision_objects, collision_events)
map_object = Tiles(tiles_path, csv_path_1, (1, 1), (16, 16), False, map_scale)
collision_map = map_ground.collision_map_objects
events_objects = map_ground.events_map_objects


sceene = 1
running = True
while running:
    clock.tick(FPS)
    an_frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((50, 50, 50))

    if sceene == 1:
        all_sprites.update(display, an_frame, animation_delay, collision_map)

        map_ground.draw(display)
        map_object.draw(display)
        all_sprites.draw(display)

        if map_ground.events_call(player) == 'library_door':
            sceene = 2

    pygame.display.update()
    if an_frame >= animation_delay:
        an_frame = 0
pygame.quit()
