import sys
import pygame
from player import Player
from tile_map import Tiles
from menu import Menu
from settings import Settings
from dialog import DialogBox


SIZE = WIDTH, HEIGHT = 1080, 720
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30
an_frame = 0
animation_delay = 8
map_scale = 2


pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption('Pygame')
display = pygame.display.set_mode(SIZE)
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
player = Player(64, 64, (150, 180))
all_sprites.add(player)
map_ground = Tiles(tiles_path, csv_path, (1, 1), (16, 16), False, map_scale, collision_objects, collision_events)
map_object = Tiles(tiles_path, csv_path_1, (1, 1), (16, 16), False, map_scale)
collision_map = map_ground.collision_map_objects
events_objects = map_ground.events_map_objects

menu = Menu(display, ui1_theme_path)
settings = Settings(display, ui2_theme_path)
dialog_box = DialogBox(display, ui1_theme_path, "Hello Friends", (100, 100), (100, 50))


scene = 1
running = True
while running:
    clock.tick(FPS)
    an_frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if scene == 1:
            menu.ui_events(event)
        elif scene == 2:
            settings.ui_events(event)
        elif scene == 3:
            dialog_box.ui_events(event)
    display.fill((50, 50, 50))

    if scene == 1:
        menu.draw(display, FPS)

        if menu.button_event(menu.play_button):
            scene = 3
        elif menu.button_event(menu.settings_button):
            scene = 2
        elif menu.button_event(menu.quit_button):
            pygame.quit()
            sys.exit()

    elif scene == 2:
        settings.draw(display, FPS)
        settings.check_box(display)

        if settings.button_event(settings.back_button):
            scene = 1
        elif settings.button_event(settings.full_screen_button):
            if settings.screen_full == "Screen full: ON":
                pygame.display.toggle_fullscreen()
            elif settings.screen_full == "Screen full: OFF":
                if settings.screen_size_option.selected_option == '(1920, 1080)':
                    pygame.display.set_mode((1920, 1080))
                elif settings.screen_size_option.selected_option == '(1080, 720)':
                    pygame.display.set_mode((1080, 720))

    elif scene == 3:
        all_sprites.update(display, an_frame, animation_delay, collision_map)

        map_ground.draw(display)
        map_object.draw(display)
        all_sprites.draw(display)

        if map_ground.events_call(player) == 'library_door':
            scene = 4

        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            scene = 1

    pygame.display.update()
    if an_frame >= animation_delay:
        an_frame = 0
pygame.quit()
