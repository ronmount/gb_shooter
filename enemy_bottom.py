import random

import pygame

snd_dir = 'media/snd/'                                  # Путь до папки со звуками
img_dir = 'media/img/'                                  # Путь до папки со спрайтами

width = 1366                                            # ширина игрового окна
height = 768                                            # высота игрового окна


# Создаем класс врага снизу
class EnemyBottom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)             # Враг - спрайт

        self.image = pygame.image.load(img_dir + 'enemy_bottom/1.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, width)          # По горизонтали - случайное положение
        self.rect.y = height - 100                      # По вертикали - снизу
