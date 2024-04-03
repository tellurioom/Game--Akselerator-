import csv
import pygame

SIZE = WIDTH, HEIGHT = 600, 400
BACKGROUND_COLOR = (255, 255, 255)
FPS = 24

tiles_path = '../source/tmw_desert_spacing.png'
csv_path = '../source/desert.csv'


class Tiles:
    def __init__(self, file_path: str, csv_file: str, size=(32, 32)):

        # класс по загрузке тайлов
        # принимает: путь к файлу с тайлами; размеры одного тайла

        self.tiles = []
        self.tiles_map = pygame.sprite.Group()
        self.map_size = (0, 0)
        self.size = size
        self.image = pygame.image.load(file_path)
        self.max_size = self.image.get_size()
        self.tile = pygame.Surface(self.size)
        self.csv_file = csv_file

    def load_tiles(self):

        # функция по загрузке тайлов из файла

        for y in range(1, self.max_size[1], self.size[1]+1):
            for x in range(1, self.max_size[0], self.size[0]+1):
                self.tile = pygame.Surface(self.size)
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

    def draw_tilemap(self, display: pygame.display, csv_file: str):

        # функция по отрисовки карты на экран
        # вызывать в основном цикле игры
        # принимает: surface="экран"; путь к файлу *.csv

        if csv_file[len(csv_file)-4:len(csv_file)] != '.csv':
            raise NameError(f'{csv_file} не является файлом с расширением *.csv')

        with open(csv_file, newline='') as csvfile:
            read = csv.reader(csvfile, delimiter=',')
            x = 0
            y = 0
            for row in read:
                x = 0
                for tile in row:
                    display.blit(self.tiles[int(tile)], (x, y))
                    x += self.size[0]
                y += self.size[1]
            self.map_size = (x * self.size[0], y * self.size[1])


pygame.init()

map = Tiles(tiles_path, csv_path)
map.load_tiles()

display = pygame.display.set_mode(map.get_map_size())
clock = pygame.time.Clock()


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    display.fill(BACKGROUND_COLOR)

    map.draw_tilemap(display, csv_path)

    pygame.display.update()
pygame.quit()
