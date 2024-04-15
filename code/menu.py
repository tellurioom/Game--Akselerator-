import pygame
import pygame_gui


class Menu:
    def __init__(self, display, theme_path):
        display_size = display.get_size()
        self.ui_manager = pygame_gui.UIManager(display_size, theme_path)

        button_rect = pygame.Rect((0, -60), (200, 50))
        settings_rect = pygame.Rect((0, 0), (200, 50))
        quit_rect = pygame.Rect((0, 60), (200, 50))

        self.play_button = pygame_gui.elements.UIButton(button_rect, 'Play', self.ui_manager, object_id='play_button', anchors={'center': 'center'})
        self.settings_button = pygame_gui.elements.UIButton(settings_rect, 'Settings', self.ui_manager, object_id='settings_button', anchors={'center': 'center'})
        self.quit_button = pygame_gui.elements.UIButton(quit_rect, 'Quit', self.ui_manager, object_id='quit_button', anchors={'center': 'center'})

    def ui_events(self, event):
        self.ui_manager.process_events(event)

    def draw(self, display, clock):
        self.ui_manager.update(clock / 1000)
        self.ui_manager.draw_ui(display)

    @staticmethod
    def button_event(button):
        return button.check_pressed()
