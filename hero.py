import pygame

ufo_width, ufo_height = 100, 80


class Ufo:
    def __init__(self, window):
        self.window = window
        self.index = 0
        self.images = [pygame.transform.scale(pygame.image.load('assets/ufo_green.png'), (ufo_width, ufo_height)),
                       pygame.transform.scale(pygame.image.load('assets/ufo_pink.png'), (ufo_width, ufo_height)),
                       pygame.transform.scale(pygame.image.load('assets/ufo_gold.png'), (ufo_width, ufo_height))]
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(300, 300))
        self.speed = 10
        self.health = 3

    def update(self):
        self.image = self.images[self.index]
        self.image = self.images[self.index]
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_a] and self.rect.x - self.speed > 0:  # left
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_d] and self.rect.x + self.speed < 1100:  # right
            self.rect.x += self.speed
        if keys_pressed[pygame.K_w] and self.rect.y - self.speed > 30:  # up
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_s] and self.rect.y - self.speed < 485:  # down
            self.rect.y += self.speed
        self.window.blit(self.image, self.rect)
