import pygame
import os


class Hp:
    def __init__(self, ufo):
        self.hp_count = ufo.health
        self.index = 1
        self.images = [pygame.transform.scale(pygame.image.load('assets/gif_hearts/frame_000.png'), (100, 27)),
                       pygame.transform.scale(pygame.image.load('assets/gif_hearts/frame_001.png'), (100, 27)),
                       pygame.transform.scale(pygame.image.load('assets/gif_hearts/frame_002.png'), (100, 27)),
                       pygame.transform.scale(pygame.image.load('assets/gif_hearts/frame_003.png'), (100, 27))]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(56.5, 20))
        self.game = True

    def update(self, window):
        self.image = self.images[self.index]
        if self.hp_count == 3:
            self.index = 0
        if self.hp_count == 2:
            self.index = 1
        if self.hp_count == 1:
            self.index = 2
        if self.hp_count == 0:
            self.index = 3
            self.game = False

        window.blit(self.image, self.rect)


class Pl:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('assets/gif_planet/frame_000.png'), (60, 60))
        self.rect = self.image.get_rect(center=(1125, 25))
        self.pl_count = 0

    def update(self, window):
        font = pygame.font.Font(None, 30)
        text = font.render(f"{self.pl_count}", True, (255, 255, 255))
        window.blit(text, (1150, 15))
        window.blit(self.image, self.rect)


class Score:
    def __init__(self):
        self.rec = int(open('score').read())
        self.new_rec_image = pygame.transform.scale(pygame.image.load('assets/new_rec.png'), (60, 48))
        self.rect = self.new_rec_image.get_rect(center=(220, 637.5))
        self.show_new_rec = False

    def update(self, window, pl):
        if self.rec < pl.pl_count:
            self.rec = pl.pl_count
            self.show_new_rec = True
            with open('score', 'w') as f:
                f.write(str(self.rec))
                f.flush()
                os.fsync(f.fileno())

        if self.show_new_rec:
            window.blit(self.new_rec_image, self.rect)

        font = pygame.font.Font(None, 50)
        text = font.render(f"Record: {self.rec}", True, (255, 255, 255))
        window.blit(text, (10, 624))
