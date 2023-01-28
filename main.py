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


def get_hit_sprite(hits_dict):
    for hit in hits_dict.values():
        return hit[0]


all_sprites = pygame.sprite.Group()                 # Создаем группу для спрайтов
mobs_sprites = pygame.sprite.Group()                # Создаем группу для спрайтов мобов
bullets_sprites = pygame.sprite.Group()             # Создаем группу для спрайтов пуль
players_sprites = pygame.sprite.Group()             # Создаем группу для спрайтов игроков

player = Player()                                   # Создаём объект класса Player
all_sprites.add(player)                             # Добавляем player группу всех спрайтов
players_sprites.add(player)                         # Добавляем игрока в группу игроков

enemy_bottom = EnemyBottom()                        # Создаём объект класса EnemyBottom
all_sprites.add(enemy_bottom)                       # Добавляем enemy_bottom группу всех спрайтов
mobs_sprites.add(enemy_bottom)                      # Добавляем enemy_bottom группу врагов
enemy_right = EnemyRight()                          # Создаём объект класса EnemyRight
all_sprites.add(enemy_right)                        # Добавляем enemy_right группу всех спрайтов
mobs_sprites.add(enemy_right)                       # Добавляем enemy_bottom группу врагов
enemy_left = EnemyLeft()                            # Создаём объект класса EnemyLeft
all_sprites.add(enemy_left)                         # Добавляем enemy_left группу всех спрайтов
mobs_sprites.add(enemy_left)                        # Добавляем enemy_bottom группу врагов
enemy_top = EnemyTop()                              # Создаём объект класса EnemyTop
all_sprites.add(enemy_top)                          # Добавляем enemy_top группу всех спрайтов
mobs_sprites.add(enemy_top)                         # Добавляем enemy_bottom группу врагов

timer = pygame.time.Clock()                         # Создаем таймер pygame

# Иногда нужно добавлять pygame.mixer.init()
pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

run = True

while run:                                          # Начинаем бесконечный цикл
    timer.tick(fps)			                        # Контроль времени (обновление игры)
    all_sprites.update()                            # Выполняем действия всех спрайтов в группе

    for event in pygame.event.get():                # Обработка ввода (события)
        if event.type == pygame.QUIT:               # Проверить закрытие окна
            run = False                             # Завершаем игровой цикл
        if event.type == pygame.KEYDOWN:            # Проверить нажатие клавиш
            if event.key == pygame.K_SPACE:         # Если нажат пробел
                player.snd_shoot.play()             # Воспроизводим звук выстрела
                bullet = Bullet(player)             # Создаем пулю передавая внутрь игрока
                all_sprites.add(bullet)             # Добавляем пулю ко всем спрайтам
                bullets_sprites.add(bullet)         # Добавляем пулю ко всем пулям

    shots = pygame.sprite.groupcollide(bullets_sprites, mobs_sprites, True, True)
    if shots:
        sprite = get_hit_sprite(shots)              # Получаем спрайт из второй группы
        sprite.snd_expl.play()                      # Воспроизводим звук скрежета

    scratch = pygame.sprite.groupcollide(mobs_sprites, players_sprites, False, False)
    if scratch:
        sprite = get_hit_sprite(scratch)            # Получаем спрайт из второй группы
        sprite.snd_scratch.play()                   # Воспроизводим звук скрежета

    screen.fill(CYAN)                               # Заливка заднего фона
    all_sprites.draw(screen)                        # Отрисовываем все спрайты
    pygame.display.update()                         # Переворачиваем экран
pygame.quit()                                       # Корректно завершаем игру
