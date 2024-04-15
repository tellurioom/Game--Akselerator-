import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
                                            text='Say Hello',
                                            manager=manager)

dropdown = pygame_gui.elements.UIDropDownMenu(['Option 1', 'Option 2', 'Option 3'], 'Option 1', pygame.Rect((100, 100), (200, 30)), manager)

clock = pygame.time.Clock()
is_running = True

while is_running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')
            if event.ui_element == dropdown:
                print(f'Selected option: {event.ui_element[dropdown].text}')

        manager.process_events(event)

    manager.update(30 / 1000)

    if hello_button.check_pressed():
        print("Pressed")

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()