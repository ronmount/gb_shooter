import pygame

from player import Player
from bullet import Bullet
from explosion import Explosion
from enemy_top import EnemyTop
from enemy_left import EnemyLeft
from enemy_right import EnemyRight
from enemy_bottom import EnemyBottom
from bg import Bg

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


def draw_hp(screen, x, y, hp_width, hp_height, player):
    green = "#32CD32"                               # Зеленый цвет
    white = "#FFFFFF"                               # Белый цвет
    rect = pygame.Rect(x, y, hp_width, hp_height)   # Создаем рамку
    fill = (player.hp / player.max_hp) * hp_width   # Считаем ширину полосы hp
    fill_rect = pygame.Rect(x, y, fill, hp_height)  # Cоздаем полосу для hp
    pygame.draw.rect(screen, green, fill_rect)      # Рисуем полосу для hp
    pygame.draw.rect(screen, white, rect, 1)        # Рисуем рамку


def draw_text(screen, text, size, x, y, color):
    font_name = pygame.font.match_font('arial')     # Выбираем тип шрифта для текста
    font = pygame.font.Font(font_name, size)        # Шрифт выбранного типа и размера
    text_image = font.render(text, True, color)     # Превращаем текст в картинку
    text_rect = text_image.get_rect()               # Задаем рамку картинки с текстом
    text_rect.center = (x, y)                       # Переносим текст в координаты
    screen.blit(text_image, text_rect)              # Рисуем текст на экране


def menu():
    screen.blit(bg.image, bg.rect)                  # Включаем задний фон
    draw_text(screen, game_name, 128, width / 2, height / 4, WHITE)
    draw_text(screen, "Arrows for move, space - fire", 44, width / 2, height / 2, WHITE)
    draw_text(screen, "Press any key to start", 36, width / 2, height * 3 / 4, WHITE)
    pygame.display.flip()                           # Отображаем содержимое на экране
    run = True
    while run:
        timer.tick(fps)                             # Тикаем игровой таймер
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # Событие закрытия окна
                pygame.quit()
            if event.type == pygame.KEYUP:          # Событие нажатия любой клавиши
                run = False


def new_mobs(count):
    for i in range(count):
        el = EnemyLeft()
        er = EnemyRight()
        et = EnemyTop()
        eb = EnemyBottom()
        all_sprites.add([el, er, et, eb])
        mobs_sprites.add([el, er, et, eb])


all_sprites = pygame.sprite.Group()                 # Создаем группу для спрайтов
mobs_sprites = pygame.sprite.Group()                # Создаем группу для спрайтов мобов
bullets_sprites = pygame.sprite.Group()             # Создаем группу для спрайтов пуль
players_sprites = pygame.sprite.Group()             # Создаем группу для спрайтов игроков

bg = Bg()                                           # Создаём объект класса Bg
all_sprites.add(bg)                                 # Добавляем bg группу всех спрайтов

player = Player()                                   # Создаём объект класса Player
all_sprites.add(player)                             # Добавляем player группу всех спрайтов
players_sprites.add(player)                         # Добавляем игрока в группу игроков

timer = pygame.time.Clock()                         # Создаем таймер pygame

# Иногда нужно добавлять pygame.mixer.init()
pygame.mixer.music.load(snd_dir + "music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

level = 1
run = True
game_over = True

while run:                                          # Начинаем бесконечный цикл
    if game_over:                                   # Если игра завершена
        level = 1                                   # Сбрасываем уровень до 1
        player.__init__()                           # Пересоздаём игрока
        for sprite in mobs_sprites:                 # Очищаем группу спрайтов
            sprite.kill()
        new_mobs(level)                             # Создаем мобов по уровню
        game_over = False                           # Запускаем новую игру
        menu()                                      # Рисуем меню

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

    shots = pygame.sprite.groupcollide(bullets_sprites, mobs_sprites, True, False)
    if shots:
        sprite = get_hit_sprite(shots)              # Получаем спрайт из второй группы
        sprite.hp -= 30                             # Отнимаем у моба 30 единиц здоровья
        if sprite.hp <= 0:                          # Если здоровья не осталось
            sprite.snd_expl.play()                  # Воспроизводим звук взрыва
            expl = Explosion(sprite.rect.center)    # Создаём объект класса Explosion
            all_sprites.add(expl)                   # Добавляем expl ко всем спрайтам
            sprite.kill()                           # Уничтожаем спрайт

    scratch = pygame.sprite.groupcollide(mobs_sprites, players_sprites, False, False)
    if scratch:
        sprite = get_hit_sprite(scratch)            # Получаем спрайт из второй группы
        sprite.snd_scratch.play()                   # Воспроизводим звук скрежета
        player.hp -= 1                              # Отнимаем у игрока единицу здоровья
        if player.hp <= 0:                          # Если здоровья не осталось
            game_over = True                        # Завершаем игру

    if len(mobs_sprites) == 0:                      # Если мобов в группе не осталось
        level += 1                                  # Увеличиваем уровень
        new_mobs(level)                             # Создаем новых мобов

    screen.fill(CYAN)                               # Заливка заднего фона
    all_sprites.draw(screen)                        # Отрисовываем все спрайты
    draw_hp(screen, 50, 50, 200, 20, player)        # Отрисовываем полоску здоровья
    pygame.display.update()                         # Переворачиваем экран
pygame.quit()                                       # Корректно завершаем игру
