import pygame


SIZE = WIDTH, HEIGHT = 1000, 600
BACKGROUND_COLOR = (255, 255, 255)
FPS = 30
source = '../source/'
animation_delay = 12


class Player(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.sprite_sheet_side = pygame.image.load(f'{source}_side idle.png').convert_alpha()
        self.sprite_sheet_down = pygame.image.load(f'{source}_down idle.png').convert_alpha()
        self.sprite_sheet_up = pygame.image.load(f'{source}_up idle.png').convert_alpha()

        self.images_frame_side = []
        y = 0
        for x in range(0, 4):
            self.image = pygame.Surface((width, height)).convert_alpha()
            self.image.blit(self.sprite_sheet_side, (0, 0), (x * width, 0, width, height))
            self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
            self.image.set_colorkey((0, 0, 0))
            self.images_frame_side.append(self.image)

        self.images_frame_down = []
        for x in range(0, 4):
            self.image = pygame.Surface((width, height)).convert_alpha()
            self.image.blit(self.sprite_sheet_down, (0, 0), (x * width, 0, width, height))
            self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
            self.image.set_colorkey((0, 0, 0))
            self.images_frame_down.append(self.image)

        self.images_frame_up = []
        for x in range(0, 4):
            self.image = pygame.Surface((width, height)).convert_alpha()
            self.image.blit(self.sprite_sheet_up, (0, 0), (x * width, 0, width, height))
            self.image = pygame.transform.scale(self.image, (width * 2, height * 2))
            self.image.set_colorkey((0, 0, 0))
            self.images_frame_up.append(self.image)

        self.rect = pygame.Rect(0, 0, width, height)
        self.frame = 0

        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5

    def update(self, display: pygame.display, frame: int):
        self.vel_x = 0
        self.vel_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.vel_y -= self.speed
        if keys[pygame.K_s]:
            self.vel_y += self.speed
        if keys[pygame.K_a]:
            self.vel_x -= self.speed
        if keys[pygame.K_d]:
            self.vel_x += self.speed

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if frame == animation_delay:
            self.frame += 1
        if self.frame >= len(self.images_frame_side):
            self.frame = 0

        if self.vel_x > 0:
            self.image = pygame.transform.flip(self.images_frame_side[self.frame], True, False)
        elif self.vel_x < 0:
            self.image = self.images_frame_side[self.frame]
        elif self.vel_y >= 0:
            self.image = self.images_frame_down[self.frame]
        elif self.vel_y < 0:
            self.image = self.images_frame_up[self.frame]


pygame.init()
pygame.display.set_caption("Pygame")
display = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player(64, 64)
all_sprites.add(player)

an_frame = 0
running = True
while running:
    clock.tick(FPS)
    an_frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill((0, 0, 0))

    all_sprites.update(display, an_frame)
    all_sprites.draw(display)
    pygame.display.update()

    if an_frame >= animation_delay: an_frame = 0
pygame.quit()
