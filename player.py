import pygame

snd_dir = 'media/snd/'            # Путь до папки со звуками
img_dir = 'media/img/'            # Путь до папки со спрайтами

width = 1366                      # ширина игрового окна
height = 768                      # высота игрового окна


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_dir + 'player/player.png')
        self.rect = self.image.get_rect()
        self.rect.center = [width/2, height/2]
