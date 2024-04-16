import csv
import json
import pygame


class Tiles:
    def __init__(self, image_file: str, csv_file: str, borders=(1, 1), size=(32, 32), start_border=True, scale=1, collision_map_file='', events_map_file=''):

        # класс по загрузке тайлов
        # принимает: путь к файлу с тайлами; размеры одного тайла

        self.files = [image_file, csv_file, collision_map_file, events_map_file]
        self.csv_file = csv_file
        try:

            if csv_file[len(csv_file) - 4:len(csv_file)] != '.csv':
                raise NameError(f'{csv_file} не является файлом с расширением *.csv')

            for files in self.files:
                if files == '':
                    break
                open(files, newline='')

        except FileNotFoundError:
            raise NameError(f'Не найден путь к файлу {files}')
        self.scale = scale
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale_by(self.image, scale)
        self.tiles = []
        self.map_size = (0, 0)
        self.size = (size[0] * scale, size[1] * scale)
        self.max_size = self.image.get_size()
        self.tile = pygame.Surface(self.size)
        self.borders = (borders[0] * scale, borders[1] * scale)
        self.start_border = start_border
        self.load_tiles()

        self.collision_map_objects = pygame.sprite.Group()
        self.events_map_objects = pygame.sprite.Group()

        if collision_map_file != '':
            self.creat_collision_map(collision_map_file)

        if events_map_file != '':
            self.creat_events_map(events_map_file)

    def load_tiles(self):

        # функция по загрузке тайлов из файла

        start_x = 1
        start_y = 1
        if not self.start_border:
            start_x = 0
            start_y = 0

        for y in range(start_y, self.max_size[1], self.size[1] + self.borders[1]):
            for x in range(start_x, self.max_size[0], self.size[0] + self.borders[0]):
                self.tile = pygame.Surface(self.size, pygame.SRCALPHA)
                self.tile.blit(self.image, (0, 0), (x, y, self.size[0], self.size[1]))
                self.tiles.append(self.tile)

    def get_map_size(self):

        # функция по получению размеров итоговой карты
        # возвращает итоговый размер карты
        # вызвать в методе display.set_mode()

        with open(self.csv_file, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            x = 0
            y = 0
            for row in read:
                x = 0
                for _ in row:
                    x += self.size[0]
                y += self.size[1]
            self.map_size = (x, y)
        return self.map_size

    def draw(self, display: pygame.display):

        # функция по отрисовки карты на экран
        # вызывать в основном цикле игры
        # принимает: surface="экран"; путь к файлу *.csv

        with open(self.csv_file, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            x = 0
            y = 0
            for row in read:
                x = 0
                for tile in row:
                    try:

                        if tile != '-1':
                            display.blit(self.tiles[int(tile)], (x, y))

                    except IndexError:
                        raise NameError(f'Размер тайла не соответсвует карте тайлов')

                    x += self.size[0]
                y += self.size[1]

    def creat_collision_map(self, file):
        with open(file, newline='') as json_data:
            data = json.load(json_data)
            js_object = data['objects']
            for options in js_object:
                sprite = pygame.sprite.Sprite()
                sprite.image = pygame.Surface((options['width'] * self.scale, options['height'] * self.scale))
                sprite.image.fill(pygame.Color('Green'))
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = options['x'] * self.scale
                sprite.rect.y = options['y'] * self.scale
                self.collision_map_objects.add(sprite)

    def creat_events_map(self, file):
        with open(file, newline='') as json_data:
            data = json.load(json_data)
            js_object = data['objects']
            for options in js_object:
                sprite = pygame.sprite.Sprite()
                sprite.image = pygame.Surface((options['width'] * self.scale, options['height'] * self.scale))
                sprite.image.fill(pygame.Color('Green'))
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = options['x'] * self.scale
                sprite.rect.y = options['y'] * self.scale
                sprite.name = options['name']
                self.events_map_objects.add(sprite)

    def events_call(self, player: pygame.sprite.Sprite):
        for hits in pygame.sprite.spritecollide(player, self.events_map_objects, False):
            return hits.name
