import pygame
import pygame_menu
from pygame_menu import themes

pygame.init()
surface = pygame.display.set_mode((600, 400))


def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)


def start_the_game():
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)


def level_menu():
    mainmenu._open(level)


mainmenu = pygame_menu.Menu('Welcome', 600, 400, theme=themes.THEME_SOLARIZED)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)
mainmenu.add.button('Play', start_the_game)
mainmenu.add.button('Levels', level_menu)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

level = pygame_menu.Menu('Select a Difficulty', 600, 400, theme=themes.THEME_BLUE)
level.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)

loading = pygame_menu.Menu('Loading the Game', 600, 400, theme=themes.THEME_DARK)
loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)
update_loading = pygame.USEREVENT + 0

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))

# running = True
# while running:
#     clock.tick(30)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     if pygame.key.get_pressed()[pygame.K_1]:
#         menu.disable()
#
#     display.fill((0, 0, 0))
#     display.blit(pygame.image.load('..source/tmw_desert_spacing.png'), (0, 0))
#     pygame.display.update()
# pygame.quit()


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == update_loading:
            progress = loading.get_widget("1")
            progress.set_value(progress.get_value() + 1)
            if progress.get_value() == 100:
                pygame.time.set_timer(update_loading, 1)
        if event.type == pygame.QUIT:
            exit()

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)
        if mainmenu.get_current().get_selected_widget():
            arrow.draw(surface, mainmenu.get_current().get_selected_widget())

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        mainmenu.disable()
        surface.fill((0, 0, 0))

    pygame.display.update()