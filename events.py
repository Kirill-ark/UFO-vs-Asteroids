from asteroid import Asteroid
from planet import Planet
from random import randint
import pygame
from sounds import boom_sound, hit_sound


def event(window, planet_group, pl, hp, ufo):
    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            pygame.quit()
            exit()

        if e.type == pygame.KEYDOWN and hp.game:
            if e.key == pygame.K_p:
                do_pause(window, ufo)

        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            x, y = e.pos

            if 1040 < x < 1190 and 610 < y < 665 and hp.game:
                do_pause(window, ufo)

            for planet in list(planet_group):
                if planet.rect.collidepoint(x, y):
                    pl.pl_count += 1
                    boom_sound()
                    planet.speed = 1


def make_asteroid(asteroid_group, window):
    asteroid_group.update()
    asteroid_group.draw(window)
    if len(asteroid_group) < 7:
        asteroid = Asteroid(randint(3, 8))
        asteroid_group.add(asteroid)


def make_planet(planet_group, window):
    planet_group.update()
    planet_group.draw(window)
    if len(planet_group) < 1:
        if randint(0, 100) == 1:
            planet = Planet(randint(7, 8))
            planet_group.add(planet)


def collide(ufo, asteroid_group, hp):
    if pygame.sprite.spritecollide(ufo, asteroid_group, True):
        hit_sound()
        hp.hp_count -= 1
        ufo.health -= 1


def finish(window, ufo):
    if ufo.health < 1:
        font = pygame.font.Font(None, 70)
        finish_text = font.render("You're dead.", True, (255, 0, 0))
        window.blit(finish_text, finish_text.get_rect(center=(600, 300)))

def draw_pause_menu(window):
    font = pygame.font.Font(None, 70)
    cont_text = font.render("Continue (P)", True, (0, 0, 0))
    skins_text = font.render("Skins", True, (0, 0, 0))
    exit_text = font.render("Exit", True, (0, 0, 0))
    pygame.draw.rect(window, (204, 204, 204), pygame.Rect(200, 100, 800, 400))  # pause menu
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(400, 140, 400, 80))  # continue button
    window.blit(cont_text, cont_text.get_rect(center=(600, 180)))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(400, 260, 400, 80))  # skins button
    window.blit(skins_text, skins_text.get_rect(center=(600, 300)))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(400, 380, 400, 80))  # exit button
    window.blit(exit_text, exit_text.get_rect(center=(600, 420)))


checkmark_pos = 1
def draw_skins_menu(window):
    pygame.draw.rect(window, (204, 204, 204), pygame.Rect(200, 100, 800, 400))
    font = pygame.font.Font(None, 70)
    back_text = font.render("Back", True, (0, 0, 0))
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(500, 410, 200, 80))  # continue button
    window.blit(back_text, back_text.get_rect(center=(600, 450)))
    im_green = pygame.transform.scale(pygame.image.load('assets/ufo_green.png'), (240, 192))
    im_pink = pygame.transform.scale(pygame.image.load('assets/ufo_pink.png'), (240, 192))
    im_gold = pygame.transform.scale(pygame.image.load('assets/ufo_gold.png'), (240, 192))
    window.blit(im_green, im_green.get_rect(center=(340, 216)))
    window.blit(im_pink, im_pink.get_rect(center=(600, 216)))
    window.blit(im_gold, im_gold.get_rect(center=(860, 216)))
    green_ind = pygame.transform.scale(pygame.image.load('assets/checkmark.png'), (50, 50))
    global checkmark_pos
    if checkmark_pos == 1:
        window.blit(green_ind, green_ind.get_rect(center=(340, 340)))
    elif checkmark_pos == 2:
        window.blit(green_ind, green_ind.get_rect(center=(600, 340)))
    elif checkmark_pos == 3:
        window.blit(green_ind, green_ind.get_rect(center=(860, 340)))

def draw_transparent_rect(surface, color, rect, alpha):
    temp = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    temp.fill((*color, alpha))
    surface.blit(temp, rect.topleft)


def do_pause(window, ufo):
    global checkmark_pos
    pause = True
    while pause:
        skins_pause = True
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            draw_pause_menu(window)
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1: # continue button
                x, y = e.pos
                if 400 < x < 800 and 140 < y < 220:
                    pause = False
                if 400 < x < 800 and 380 < y < 460:
                    pygame.quit()
                    exit()
                if 400 < x < 800 and 260 < y < 340:
                    while skins_pause:
                        for e in pygame.event.get():
                            draw_skins_menu(window)
                            if e.type == pygame.QUIT:
                                pygame.quit()
                                exit()
                            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:  # exit button
                                x, y = e.pos
                                if 500 < x < 700 and 410 < y < 490:
                                    skins_pause = False
                                if 220 < x < 460 and 209 < y < 305:
                                    draw_transparent_rect(window, (255, 255, 255), pygame.Rect(220, 115, 240, 200), 120)
                                    checkmark_pos = 1
                                    ufo.index = 0
                                if 480 < x < 720 and 209 < y < 305:
                                    draw_transparent_rect(window, (255, 255, 255), pygame.Rect(480, 115, 240, 200), 120)
                                    checkmark_pos = 2
                                    ufo.index = 1
                                if 740 < x < 980 and 209 < y < 305:
                                    draw_transparent_rect(window, (255, 255, 255), pygame.Rect(740, 115, 240, 200), 120)
                                    checkmark_pos = 3
                                    ufo.index = 2
                        pygame.display.update()
            if e.type == pygame.KEYDOWN: # exit pause menu with p
                if e.key == pygame.K_p:
                    pause = False
        pygame.display.update()
