import pygame
import pymunk.pygame_util
import random
import math


SIZE = WIDTH, HEIGHT = 1000, 600
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30


pygame.init()
pymunk.pygame_util.positive_y_is_up = False


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.orig_image = pygame.Surface((50, 100), pygame.SRCALPHA)
        self.orig_image.fill((0, 255, 0))
        self.orig_image = pygame.transform.scale(self.orig_image, self.orig_image.get_size())
        self.image = self.orig_image.copy()
        self.rect = self.image.get_rect(center=(500, 500))

        self.vel = 0
        self.angle = 0
        self.vel_speed = 5
        self.rotate_speed = 10

        self.space = pymunk.Space
        self.body = pymunk.Body
        self.shape = pymunk.Poly

    def update(self, display):
        self.vel = 0
        event_key = pygame.key.get_pressed()
        if event_key[pygame.K_UP]:
            self.vel -= self.vel_speed
        if event_key[pygame.K_DOWN]:
            self.vel += self.vel_speed
        if event_key[pygame.K_LEFT]:
            self.angle += self.rotate_speed
        if event_key[pygame.K_RIGHT]:
            self.angle -= self.rotate_speed

        self.body.position += ((self.vel * math.sin(math.radians(self.angle)),
                                self.vel * math.cos(math.radians(self.angle))))
        self.rect.center = self.body.position
        self.body.angle = -math.radians(self.angle)

        self.image = pygame.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        display.blit(self.image, self.rect)

    def physics(self, pm_space):
        size = self.rect.size
        mass = 5
        moment = pymunk.moment_for_box(mass, size)
        self.body = pymunk.Body(mass, moment)
        self.shape = pymunk.Poly.create_box(self.body, size)
        self.shape.elasticity = 1
        self.shape.friction = 2
        self.body.position = self.rect.center
        self.space = pm_space
        self.space.add(self.body, self.shape)


pygame.display.set_caption("Pygame")
display = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

draw_option = pymunk.pygame_util.DrawOptions(display)
space = pymunk.Space()
space.gravity = (0, 0)

segment_shape = pymunk.Segment(space.static_body, (100, 200), (400, 200), 45)
space.add(segment_shape)
segment_shape.elasticity = 1
segment_shape.friction = 1

all_sprites = pygame.sprite.Group()
player = Player()
player.physics(space)
all_sprites.add(player)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((255, 255, 255))

    space.step(1 / FPS)
    all_sprites.update(display)
    all_sprites.draw(display)
    pygame.draw.rect(display, (0, 0, 0), (60, 160, 380, 80))

    pygame.display.update()
pygame.quit()