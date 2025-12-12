import pygame
from random import randint
import background as bg

# images_explosion = [
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_000.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_001.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_002.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_003.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_004.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_005.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_006.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_007.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_008.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_009.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_010.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_011.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_012.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_013.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_014.png')), (90, 100)),
#             pygame.transform.scale((pygame.image.load('assets/gif_explosion/frame_015.png')), (90, 100))]
images_moving = [
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_000.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_001.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_002.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_003.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_004.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_005.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_006.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_planet/frame_007.png')), (100, 100))]
images_explosion = [
    pygame.transform.scale((pygame.image.load('assets/gif_explosion2/frame_000.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_explosion2/frame_001.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_explosion2/frame_002.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_explosion2/frame_003.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_explosion2/frame_004.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_explosion2/frame_005.png')), (100, 100)),
    pygame.transform.scale((pygame.image.load('assets/gif_explosion2/frame_006.png')), (100, 100))]


class Planet(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.index_moving = 0
        self.index_exp = 0
        self.images = images_moving
        self.image = self.images[self.index_moving]
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = bg.width
        self.rect.y = randint(100, 530)

    def update(self):
        if self.speed > 1:
            self.image = self.images[self.index_moving // 6]
            self.rect.x -= self.speed
            if self.index_moving < 42:
                self.index_moving += 1
            else:
                self.index_moving = 0
        else:
            self.images = images_explosion
            self.image = self.images[self.index_exp // 3]
            self.rect.x -= self.speed
            if self.index_exp < 18:
                self.index_exp += 1
            else:
                self.kill()
                self.index_exp = 0
                self.images = images_moving

        if self.rect.x < -100:
            self.kill()
