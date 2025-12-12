import pygame

pygame.mixer.init()


def bcg_music():
    pygame.mixer.music.load('assets/bcg_music.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)


def boom_sound():
    boom = pygame.mixer.Sound('assets/boom_sound.mp3')
    boom.play()


def hit_sound():
    hit = pygame.mixer.Sound('assets/hit_sound.mp3')
    hit.play()
