import pygame
import pygame.time

# Инициализация Pygame
pygame.init()

event_1 = pygame.USEREVENT + 1
event_2 = pygame.USEREVENT + 2

# Установка интервалов времени в миллисекундах
pygame.time.set_timer(event_1, 1000)  # Таймер для первого сообщения (1 секунда)
pygame.time.set_timer(event_2, 2000)  # Таймер для второго сообщения (2 секунды)

# Создание переменных для хранения сообщений и флагов для отображения
message1 = ""
message2 = ""
show_message1 = False
show_message2 = False

# Главный цикл программы
running = True
while running:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == event_1:
            if show_message1:
                show_message1 = False
            else:
                show_message1 = True
        if event.type == event_2:
            if show_message2:
                show_message2 = False
            else:
                show_message2 = True

    # Отображение сообщений на экране
    screen = pygame.display.set_mode((600, 300))
    screen.fill((0, 0, 0))  # Очистка экрана

    if show_message1:
        message1 = "Первое сообщение каждую секунду"
        font = pygame.font.Font(None, 36)
        text1 = font.render(message1, True, (255, 255, 255))
        screen.blit(text1, (10, 50))

    if show_message2:
        message2 = "Второе сообщение каждые две секунды"
        font = pygame.font.Font(None, 36)
        text2 = font.render(message2, True, (255, 255, 255))
        screen.blit(text2, (10, 200))

    pygame.display.flip()
pygame.quit()
