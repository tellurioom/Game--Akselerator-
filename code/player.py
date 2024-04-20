import pygame


source = '../source/'
image_scale = 2


class Player(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, spawn=(0, 0)):
        super().__init__()

        self.sprite_sheet_idle = pygame.image.load(f'{source}Adam_idle_anim_16x16.png').convert_alpha()
        self.sprite_sheet_walk = pygame.image.load(f'{source}Adam_run_16x16.png').convert_alpha()

        self.images_frame_idle = []
        self.images_frame_walk = []

        for x in range(0, 24):
            self.image = pygame.Surface((width, height))
            self.image.blit(self.sprite_sheet_idle, (0, 0), (x * width, 8, width, height-8))
            self.image = pygame.transform.scale_by(self.image, image_scale)
            self.image.set_colorkey((0, 0, 0))
            self.images_frame_idle.append(self.image)

        for x in range(0, 24):
            self.image = pygame.Surface((width, height))
            self.image.blit(self.sprite_sheet_walk, (0, 0), (x * width, 8, width, height-8))
            self.image = pygame.transform.scale_by(self.image, image_scale)
            self.image.set_colorkey((0, 0, 0))
            self.images_frame_walk.append(self.image)

        self.rect = pygame.Rect(spawn, (16 * image_scale, 24 * image_scale))
        self.rect.center = spawn
        self.frame = 0
        self.last_direction = 2
        self.action = [0, 6, 12, 18]

        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5 * (image_scale / 2)

    def update(self, display: pygame.display, frame: int, animation_delay: int, collide_objects, size_scale : float):
        self.vel_x = 0
        self.vel_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.vel_y -= self.speed * size_scale
            self.last_direction = 1
        if keys[pygame.K_s]:
            self.vel_y += self.speed * size_scale
            self.last_direction = 3
        if keys[pygame.K_a]:
            self.vel_x -= self.speed * size_scale
            self.last_direction = 2
        if keys[pygame.K_d]:
            self.vel_x += self.speed * size_scale
            self.last_direction = 0

        self.move(self.rect, (self.vel_x, self.vel_y), collide_objects)
        self.animation(frame, animation_delay)

    def animation(self, frame, animation_delay):
        if frame == animation_delay:
            self.frame += 1
            if self.frame >= 6:
                self.frame = 0

        if self.vel_x != 0 or self.vel_y != 0:
            self.image = self.images_frame_walk[self.frame + self.action[self.last_direction]]
        else:
            self.image = self.images_frame_idle[self.frame + self.action[self.last_direction]]

    def collision_test(self, rect, tiles):
        collisions = []
        for tile in tiles:
            if rect.colliderect(tile.rect):
                collisions.append(tile.rect)
        return collisions

    def move(self, rect, movement, tiles):
        self.rect.x += movement[0]
        collisions = self.collision_test(rect, tiles)
        for tile in collisions:
            if self.vel_x > 0:
                self.rect.right = tile.left
            if self.vel_x < 0:
                self.rect.left = tile.right
        self.rect.y += movement[1]
        collisions = self.collision_test(rect, tiles)
        for tile in collisions:
            if self.vel_y > 0:
                self.rect.bottom = tile.top
            if self.vel_y < 0:
                self.rect.top = tile.bottom

    def draw(self, display, screen_scale):
        scale_image = pygame.transform.scale_by(self.image, screen_scale)
        display.blit(scale_image, (self.rect.x, self.rect.y))
