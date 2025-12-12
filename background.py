import pygame

width, height = 1200, 675


class Background:
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load('assets/space.jpg'), (width, height))
        self.rect = self.image.get_rect()
        self.moving_speed = 1
        self.bcgx1 = 0
        self.bcgy1 = 0
        self.bcgx2 = self.rect.width
        self.bcgy2 = 0

    def update(self):
        self.bcgx1 -= self.moving_speed
        self.bcgx2 -= self.moving_speed

        if self.bcgx1 <= - self.rect.width:
            self.bcgx1 = self.rect.width
        if self.bcgx2 <= - self.rect.width:
            self.bcgx2 = self.rect.width

    def render(self, window):
        window.blit(self.image, (self.bcgx1, self.bcgy1))
        window.blit(self.image, (self.bcgx2, self.bcgy2))
