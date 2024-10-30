import pygame
import time
import random

pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREY = (224, 224, 224)
DARKGREY = (64, 64, 64)

# Параметры окна
WIDTH = 600
HEIGHT = 400
BLOCK_SIZE = 10

# Инициализация окна
pygame.display.set_caption('Змейка')
game_window = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, GREEN, [x[0], x[1], block_size, block_size])

def message(msg, color):
    # Разбиваем сообщение на строки
    lines = msg.splitlines()
    for i, line in enumerate(lines):
        mesg = font_style.render(line, True, color)
        game_window.blit(mesg, [WIDTH / 6, HEIGHT / 3 + i * 30])  # Сдвигаем каждую строку вниз


def game_loop():
    game_over = False
    game_close = False

    x1 = WIDTH / 2
    y1 = HEIGHT / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            game_window.fill(DARKGREY)
            message("Ты проиграл!\nНажми C, чтобы играть снова\nили Q, чтобы выйти.", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0

        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_window.fill(GREY)
        pygame.draw.rect(game_window, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(BLOCK_SIZE, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1

        clock.tick(10)

    pygame.quit()

game_loop()