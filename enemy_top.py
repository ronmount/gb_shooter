import random

import pygame

snd_dir = 'media/snd/'                                  # Путь до папки со звуками
img_dir = 'media/img/'                                  # Путь до папки со спрайтами

width = 1366                                            # ширина игрового окна
height = 768                                            # высота игрового окна


# Создаем класс врага сверху
class EnemyTop(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)             # Враг - спрайт

        self.image = pygame.image.load(img_dir + 'enemy_top/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)          # По горизонтали - случайное положение
        self.rect.y = 0                                 # По вертикали - сверху
