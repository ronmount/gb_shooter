import pygame

from player import Player
from bullet import Bullet
from explosion import Explosion
from enemy_top import EnemyTop
from enemy_left import EnemyLeft
from enemy_right import EnemyRight
from enemy_bottom import EnemyBottom

pygame.init()                                       # Инициализируем модуль pygame

width = 1366                                        # ширина игрового окна
height = 768                                        # высота игрового окна
fps = 30                                            # частота кадров в секунду
game_name = "Shooter"                               # название нашей игры

# Цвета
BLACK = "#000000"
WHITE = "#FFFFFF"
RED = "#FF0000"
GREEN = "#008000"
BLUE = "#0000FF"
CYAN = "#00FFFF"

snd_dir = 'media/snd/'                              # Путь до папки со звуками
img_dir = 'media/img/'                              # Путь до папки со спрайтами

# Создаем игровой экран
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(game_name)               # Заголовок окна

icon = pygame.image.load(img_dir + 'icon.png')      # Загружаем файл с иконкой
pygame.display.set_icon(icon)                       # Устанавливаем иконку в окно

all_sprites = pygame.sprite.Group()                 # Создаем группу для спрайтов

player = Player()                                   # Создаём объект класса Player
all_sprites.add(player)                             # Добавляем player группу всех спрайтов
enemy_bottom = EnemyBottom()                        # Создаём объект класса EnemyBottom
all_sprites.add(enemy_bottom)                       # Добавляем enemy_bottom группу всех спрайтов
enemy_right = EnemyRight()                          # Создаём объект класса EnemyRight
all_sprites.add(enemy_right)                        # Добавляем enemy_right группу всех спрайтов
enemy_left = EnemyLeft()                            # Создаём объект класса EnemyLeft
all_sprites.add(enemy_left)                         # Добавляем enemy_left группу всех спрайтов
enemy_top = EnemyTop()                              # Создаём объект класса EnemyTop
all_sprites.add(enemy_top)                          # Добавляем enemy_top группу всех спрайтов

timer = pygame.time.Clock()                         # Создаем таймер pygame
run = True

while run:                                          # Начинаем бесконечный цикл
    timer.tick(fps)			                        # Контроль времени (обновление игры)
    all_sprites.update()                            # Выполняем действия всех спрайтов в группе

    for event in pygame.event.get():                # Обработка ввода (события)
        if event.type == pygame.QUIT:               # Проверить закрытие окна
            run = False                             # Завершаем игровой цикл

    screen.fill(CYAN)                               # Заливка заднего фона
    all_sprites.draw(screen)                        # Отрисовываем все спрайты
    pygame.display.update()                         # Переворачиваем экран
pygame.quit()                                       # Корректно завершаем игру
