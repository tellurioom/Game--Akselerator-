import pygame
import pygame_gui


text = f'Съешь ещё этих мягких французских булок,\nда выпей же чаю.'


class Settings:
    def __init__(self, display, theme_path):
        display_size = display.get_size()
        self.ui_manager = pygame_gui.UIManager(display_size, theme_path)

        s1_rect = pygame.Rect((0, -60), (200, 50))
        s2_rect = pygame.Rect((0, 0), (200, 50))
        s3_rect = pygame.Rect((10, 10), (30, 30))
        b_button_rect = pygame.Rect((0, 300), (200, 50))

        self.screen_full = 'Screen full: OFF'
        self.screen_size = ['(1920, 1080)', '(1080, 720)']
        self.full_screen_button = pygame_gui.elements.UIButton(s1_rect, self.screen_full, self.ui_manager, anchors={'center': 'center'})
        self.screen_size_option = pygame_gui.elements.UIDropDownMenu(self.screen_size, '(1080, 720)',  s2_rect, self.ui_manager, anchors={'center': 'center'})
        self.back_button = pygame_gui.elements.UIButton(b_button_rect, 'Back', self.ui_manager, object_id='back_button', anchors={'center': 'center', 'bottom': 'bottom'})
        self.check_box_button = pygame_gui.elements.UIButton(s3_rect, '', self.ui_manager, anchors={'left': 'left', 'top': 'top'})

        self.music_enable = True

    def ui_events(self, event):
        self.ui_manager.process_events(event)

    def draw(self, display, clock):
        self.ui_manager.update(clock / 1000)
        self.ui_manager.draw_ui(display)
        self.change_screen_full()
        self.full_screen_button.set_text(self.screen_full)

    @staticmethod
    def button_event(button):
        return button.check_pressed()

    def change_screen_full(self):
        if self.full_screen_button.check_pressed() and self.screen_full == "Screen full: OFF":
            self.screen_full = "Screen full: ON"
        elif self.full_screen_button.check_pressed() and self.screen_full == "Screen full: ON":
            self.screen_full = "Screen full: OFF"

    def check_box(self, display):
        box_rect = pygame.Rect((10, 10), (30, 30))
        sprite = pygame.Surface((30, 30))
        if self.music_enable:
            sprite.fill(pygame.Color('Green'))
        elif not self.music_enable:
            sprite.fill(pygame.Color('Red'))

        if self.check_box_button.check_pressed():
            self.music_enable = not self.music_enable

        display.blit(sprite, box_rect)
