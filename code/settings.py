import pygame
import pygame_gui


text = f'Съешь ещё этих мягких французских булок,\nда выпей же чаю.'


class Settings:
    def __init__(self, display, theme_path):
        display_size = display.get_size()
        self.ui_manager = pygame_gui.UIManager(display_size, theme_path)

        s1_rect = pygame.Rect((0, -60), (300, 50))
        s2_rect = pygame.Rect((0, 0), (200, 50))
        s3_rect = pygame.Rect((0, 60), (200, 50))
        s4_rect = pygame.Rect((0, 200), (200, 10))

        self.s1 = pygame_gui.elements.UIHorizontalSlider(start_value=0, value_range=(0, 1), relative_rect=s1_rect, manager=self.ui_manager, anchors={'center': 'center'})
        self.s2 = pygame_gui.elements.UIProgressBar(relative_rect=s2_rect, manager=self.ui_manager, anchors={'center': 'center'})
        self.s3 = pygame_gui.elements.UIDropDownMenu(['option_1', 'option_2', 'option_3'], 'option_1', s3_rect, self.ui_manager, anchors={'center': 'center'})
        self.s4 = pygame_gui.elements.UITextBox(text, s4_rect, self.ui_manager, wrap_to_height=True, anchors={'center': 'center'})

    def ui_events(self, event):
        self.ui_manager.process_events(event)

    def draw(self, display, clock):
        self.ui_manager.update(clock / 1000)
        self.ui_manager.draw_ui(display)

    @staticmethod
    def button_event(button):
        return button.check_pressed()
