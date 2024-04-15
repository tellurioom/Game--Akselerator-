import pygame
import pygame_gui


class DialogBox:
    def __init__(self, display, theme_path, text='', text_pos=(0, 0), box_size=(0, 0)):
        display_size = display.get_size()
        self.ui_manager = pygame_gui.UIManager(display_size, theme_path)

        box_rect = pygame.Rect(text_pos, box_size)
        self.text_box = pygame_gui.elements.UITextBox(text, box_rect, self.ui_manager, wrap_to_height=True)

        box_button_rect = pygame.Rect((self.text_box.rect.x, self.text_box.rect.bottom), (self.text_box.rect.width, 40))
        self.button_close = pygame_gui.elements.UIButton(box_button_rect, 'Close', self.ui_manager)

    def ui_events(self, event):
        self.ui_manager.process_events(event)

    def draw(self, display, clock):
        self.ui_manager.update(clock / 1000)
        self.ui_manager.draw_ui(display)

    @staticmethod
    def button_event(button):
        return button.check_pressed()

