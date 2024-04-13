import csv
import pygame


class Tiles:
    def __init__(self, file_path: str, csv_file: str, borders=(1, 1), size=(32, 32), start_border=True, scale=1):

        # класс по загрузке тайлов
        # принимает: путь к файлу с тайлами; размеры одного тайла

        try:

            self.image = pygame.image.load(file_path)
            self.image = pygame.transform.scale_by(self.image, scale)

        except FileNotFoundError:
            raise NameError(f'Не найден путь к файлу {file_path}')

        self.tiles = []
        self.map_size = (0, 0)
        self.size = (size[0] * scale, size[1] * scale)
        self.max_size = self.image.get_size()
        self.tile = pygame.Surface(self.size)
        self.csv_file = csv_file
        self.borders = (borders[0] * scale, borders[1] * scale)
        self.start_border = start_border

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

        try:

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

        except FileNotFoundError:
            raise NameError(f'Не найден путь к файлу {self.csv_file}')

    def draw_map(self, display: pygame.display):

        # функция по отрисовки карты на экран
        # вызывать в основном цикле игры
        # принимает: surface="экран"; путь к файлу *.csv

        if self.csv_file[len(self.csv_file) - 4:len(self.csv_file)] != '.csv':
            raise NameError(f'{self.csv_file} не является файлом с расширением *.csv')

        try:

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

        except FileNotFoundError:
            raise NameError(f'Не найден путь к файлу {self.csv_file}')