import pygame
from sceen_1 import sceen_1
from sceen_2 import sceen_2


SIZE = WIDTH, HEIGHT = 1000, 600
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30


pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.display.set_caption('Pygame')
display = pygame.display.set_mode((1400, 900))
clock = pygame.time.Clock()


sceen = 1
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((50, 50, 50))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        sceen = 1
    if keys[pygame.K_2]:
        sceen = 2

    if sceen == 1:
        sceen_1(display)
    if sceen == 2:
        sceen_2(display)


    pygame.display.update()
pygame.quit()