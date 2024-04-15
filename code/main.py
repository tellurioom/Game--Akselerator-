import sys
import pygame
import pygame_gui
from Player import Player
from Tile_map import Tiles
from menu import Menu
from settings import Settings
from dialog import DialogBox


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
tiles_path = f'{source}tilemap.png'
csv_path = f'{source}sity._ground.csv'
csv_path_1 = f'{source}sity._object.csv'
collision_objects = f'{source}collision_map.json'
collision_events = f'{source}events_objects.json'
ui1_theme_path = f'{source}theme_1.json'
ui2_theme_path = f'{source}theme_2.json'

all_sprites = pygame.sprite.Group()
player = Player(64, 64, (800, 800))
all_sprites.add(player)
map_ground = Tiles(tiles_path, csv_path, (1, 1), (16, 16), False, map_scale, collision_objects, collision_events)
map_object = Tiles(tiles_path, csv_path_1, (1, 1), (16, 16), False, map_scale)
collision_map = map_ground.collision_map_objects
events_objects = map_ground.events_map_objects

menu = Menu(display, ui1_theme_path)
settings = Settings(display, ui2_theme_path)
dialog_box = DialogBox(display, ui1_theme_path, "Hello Friends", (100, 100), (100, 50))
print(menu.quit_button.get_object_ids(), settings.back_button.get_object_ids())

scene = 1
running = True
while running:
    clock.tick(FPS)
    an_frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print('quit')
        menu.ui_events(event)
        settings.ui_events(event)
        dialog_box.ui_events(event)
    display.fill((50, 50, 50))

    if scene == 1:
        menu.draw(display, FPS)

        if menu.button_event(menu.play_button):
            scene = 3
        elif menu.button_event(menu.settings_button):
            scene = 2
        elif menu.button_event(menu.quit_button):
            print('quit_button')
            pygame.quit()
            sys.exit()

    elif scene == 2:
        settings.draw(display, FPS)

        if settings.button_event(settings.back_button):
            print('back_button')
            scene = 1

    elif scene == 3:
        all_sprites.update(display, an_frame, animation_delay, collision_map)

        map_ground.draw(display)
        map_object.draw(display)
        all_sprites.draw(display)

        if map_ground.events_call(player) == 'library_door':
            scene = 4

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            scene = 1

    pygame.display.update()
    if an_frame >= animation_delay:
        an_frame = 0
pygame.quit()
