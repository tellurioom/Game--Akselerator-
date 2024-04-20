import pygame
import pygame_gui


text = f'Съешь ещё этих мягких французских булок,\nда выпей же чаю.'


class Settings:
    def __init__(self, display, theme_path, path_image):
        display_size = display.get_size()
        self.ui_manager = pygame_gui.UIManager(display_size, theme_path)

        s1_rect = pygame.Rect((0, -60), (200, 50))
        s2_rect = pygame.Rect((0, 0), (200, 50))
        s3_rect = pygame.Rect((10, 10), (30, 30))
        b_button_rect = pygame.Rect((0, 300), (200, 50))

        self.screen_full = 'Screen full: OFF'
        self.screen_size = ['1920 x 1080', '1280 x 720']
        self.full_screen_button = pygame_gui.elements.UIButton(s1_rect, self.screen_full, self.ui_manager, anchors={'center': 'center'})
        self.screen_size_option = pygame_gui.elements.UIDropDownMenu(self.screen_size, '1280 x 720',  s2_rect, self.ui_manager, anchors={'center': 'center'})
        self.back_button = pygame_gui.elements.UIButton(b_button_rect, 'Back', self.ui_manager, object_id='back_button', anchors={'center': 'center', 'bottom': 'bottom'})
        self.check_box_button = pygame_gui.elements.UIButton(s3_rect, '', self.ui_manager, anchors={'left': 'left', 'top': 'top'})

        self.music_enable = True
        self.new_display_size = display_size
        self.path_image = path_image

    def ui_events(self, event):
        self.ui_manager.process_events(event)

    def draw(self, display, clock, screen_scale):
        self.ui_manager.update(clock / 1000)
        self.ui_manager.draw_ui(display)
        self.ui_manager.set_window_resolution(display.get_size())
        self.change_screen_full()
        self.full_screen_button.set_text(self.screen_full)

        self.draw_text(display, 'Music', (50, 10))

        if self.screen_size_option.selected_option == '1920 x 1080':
            self.new_display_size = (1920, 1080)
        elif self.screen_size_option.selected_option == '1280 x 720':
            self.new_display_size = (1280, 720)

        if not pygame.display.is_fullscreen():
            self.screen_full = 'Screen full: OFF'

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

        if self.check_box_button.check_pressed():
            self.music_enable = not self.music_enable

        if self.music_enable:
            sprite = pygame.image.load(self.path_image[0]).convert_alpha()
        elif not self.music_enable:
            sprite = pygame.image.load(self.path_image[1]).convert_alpha()
        display.blit(sprite, box_rect)

    def draw_text(self, display, text, pos):
        font_text = pygame.font.SysFont('Comic Sans MS', 20)
        text_surface = font_text.render(text, False, pygame.Color('White'))
        display.blit(text_surface, pos)
