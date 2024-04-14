import pygame


source = '../source/'
image_scale = 1


class Player(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, spawn=(0, 0)):
        super().__init__()
        self.sprite_sheet_side_idle = pygame.image.load(f'{source}_side idle.png').convert_alpha()
        self.sprite_sheet_down_idle = pygame.image.load(f'{source}_down idle.png').convert_alpha()
        self.sprite_sheet_up_idle = pygame.image.load(f'{source}_up idle.png').convert_alpha()
        self.sprite_sheet_side_walk = pygame.image.load(f'{source}_side walk.png').convert_alpha()
        self.sprite_sheet_down_walk = pygame.image.load(f'{source}_down walk.png').convert_alpha()
        self.sprite_sheet_up_walk = pygame.image.load(f'{source}_up walk.png').convert_alpha()

        self.pack_sheet_side = [self.sprite_sheet_side_idle, self.sprite_sheet_side_walk]
        self.pack_sheet_down = [self.sprite_sheet_down_idle, self.sprite_sheet_down_walk]
        self.pack_sheet_up = [self.sprite_sheet_up_idle, self.sprite_sheet_up_walk]

        self.images_frame_side = []
        self.images_frame_down = []
        self.images_frame_up = []

        for sheet in self.pack_sheet_side:
            for y in range(0, 2):
                for x in range(0, 4):
                    if y == 1 and x > 0:
                        break
                    self.image = pygame.Surface((width, height))
                    self.image.blit(sheet, (0, 0), (x * width, y * height, width, height))
                    self.image = pygame.transform.scale_by(self.image, image_scale)
                    self.image.set_colorkey((0, 0, 0))
                    self.images_frame_side.append(self.image)

        for sheet in self.pack_sheet_down:
            for y in range(0, 2):
                for x in range(0, 4):
                    if y == 1 and x > 0:
                        break
                    self.image = pygame.Surface((width, height))
                    self.image.blit(sheet, (0, 0), (x * width, y * height, width, height))
                    self.image = pygame.transform.scale_by(self.image, image_scale)
                    self.image.set_colorkey((0, 0, 0))
                    self.images_frame_down.append(self.image)

        for sheet in self.pack_sheet_up:
            for y in range(0, 2):
                for x in range(0, 4):
                    if y == 1 and x > 0:
                        break
                    self.image = pygame.Surface((width, height))
                    self.image.blit(sheet, (0, 0), (x * width, y * height, width, height))
                    self.image = pygame.transform.scale_by(self.image, image_scale)
                    self.image.set_colorkey((0, 0, 0))
                    self.images_frame_up.append(self.image)

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = spawn
        self.frame = 0
        self.last_direction = 2
        self.action = {'idle': 0, 'walk': 5}

        self.vel_x = 0
        self.vel_y = 0
        self.speed = 5 * (image_scale / 2)

    def update(self, display: pygame.display, frame: int, animation_delay: int, collide_objects):
        self.vel_x = 0
        self.vel_y = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.vel_y -= self.speed
            self.last_direction = 0
        if keys[pygame.K_s]:
            self.vel_y += self.speed
            self.last_direction = 2
        if keys[pygame.K_a]:
            self.vel_x -= self.speed
            self.last_direction = 3
        if keys[pygame.K_d]:
            self.vel_x += self.speed
            self.last_direction = 1

        self.move(self.rect, (self.vel_x, self.vel_y), collide_objects)
        self.animation(frame, animation_delay)

    def animation(self, frame, animation_delay):
        if frame == animation_delay:
            self.frame += 1
            if self.frame >= 5:
                self.frame = 0

        if self.last_direction == 0:
            if self.vel_y == 0:
                self.image = self.images_frame_up[self.frame + self.action['idle']]
            else:
                self.image = self.images_frame_up[self.frame + self.action['walk']]

        elif self.last_direction == 1:
            if self.vel_x == 0:
                self.image = pygame.transform.flip(self.images_frame_side[self.frame + self.action['idle']], True, False)
            else:
                self.image = pygame.transform.flip(self.images_frame_side[self.frame + self.action['walk']], True,False)

        elif self.last_direction == 2:
            if self.vel_y == 0:
                self.image = self.images_frame_down[self.frame + self.action['idle']]
            else:
                self.image = self.images_frame_down[self.frame + self.action['walk']]

        elif self.last_direction == 3:
            if self.vel_x == 0:
                self.image = self.images_frame_side[self.frame + self.action['idle']]
            else:
                self.image = self.images_frame_side[self.frame + self.action['walk']]

    def collision_test(self, rect, tiles):
        collisions = []
        for tile in tiles:
            if rect.colliderect(tile.rect):
                collisions.append(tile.rect)
        return collisions

    def move(self, rect, movement, tiles):  # movement = [5,2]
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
