import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Setup display and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Start Menu Example")
clock = pygame.time.Clock()


def main_menu():
    while True:
        screen.fill(WHITE)

        draw_text("Welcome to My Game", 40, WIDTH / 2, HEIGHT / 4)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(WIDTH / 2 - 70, HEIGHT / 2, 140, 50)
        button_2 = pygame.Rect(WIDTH / 2 - 70, HEIGHT / 2 + 60, 140, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        pygame.draw.rect(screen, RED, button_1)
        pygame.draw.rect(screen, GREEN, button_2)

        draw_text("Play", 30, WIDTH / 2, HEIGHT / 2 + 25)
        draw_text("Options", 30, WIDTH / 2, HEIGHT / 2 + 85)

        click = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.flip()
        clock.tick(60)


def game():
    # Main game loop
    pass


def options():
    # Options menu
    pass


def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


main_menu()
