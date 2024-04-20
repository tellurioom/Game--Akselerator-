import pygame
from player import Player
from tile_map import Tiles


map_scale = 2

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


def game_play(display, an_frame, animation_delay):

    all_sprites.update(display, an_frame, animation_delay, collision_map)

    map_ground.draw_map(display)
    map_object.draw_map(display)
    all_sprites.draw(display)

    map_ground.events_call(player)
