import drawwindow
import background as bcg
import hero as hr
import indicators as hp_pl_sc
import pygame
from sounds import bcg_music
import events


def main():
    bcg_music()
    pygame.init()
    window = pygame.display.set_mode((bcg.width, bcg.height))
    pygame.display.set_caption('UFO VS ASTEROIDS')
    menu_bcg = pygame.Rect(0, 600, bcg.width, 100)
    background = bcg.Background()
    ufo = hr.Ufo(window)
    hp = hp_pl_sc.Hp(ufo)
    pl = hp_pl_sc.Pl()
    sc = hp_pl_sc.Score()
    asteroid_group = pygame.sprite.Group()
    planet_group = pygame.sprite.Group()
    clock = pygame.time.Clock()
    fps = 60
    while True:
        events.event(window, planet_group, pl, hp, ufo)
        if hp.game:
            drawwindow.draw_window(window, background, menu_bcg, ufo, asteroid_group, planet_group, hp, pl, sc)
        clock.tick(fps)
        pygame.display.flip()


if __name__ == '__main__':
    main()
