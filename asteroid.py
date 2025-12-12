import pygame
from random import randint
import background as bg


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.index = 0
        self.images = [pygame.image.load('assets/gif_asteroid/frame_000.png'),
                       pygame.image.load('assets/gif_asteroid/frame_001.png'),
                       pygame.image.load('assets/gif_asteroid/frame_002.png'),
                       pygame.image.load('assets/gif_asteroid/frame_003.png')]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = bg.width
        self.rect.y = randint(100, 550)

    def update(self):
        self.image = self.images[self.index // 5]
        self.rect.x -= self.speed
        if self.index < 15:
            self.index += 1
        else:
            self.index = 0

        if self.rect.x < -100:
            self.kill()
