import events
import pygame


def draw_window(window, background, menu_bcg, ufo, asteroid_group, planet_group, hp, pl, sc):
    background.update()
    background.render(window)
    pygame.draw.rect(window, (29, 41, 81), menu_bcg)
    pygame.draw.line(window, (255, 255, 255), (0, 599), (1200, 599), 3)
    pygame.draw.rect(window, (255, 255, 255), pygame.Rect(1040, 610, 150, 55))
    font = pygame.font.Font(None, 40)
    pause_button_text = font.render("Pause (P)", True, (0, 0, 0))
    window.blit(pause_button_text, pause_button_text.get_rect(center=(1115, 637.5)))
    sc.update(window, pl)
    events.make_planet(planet_group, window)
    events.make_asteroid(asteroid_group, window)
    events.collide(ufo, asteroid_group, hp)
    hp.update(window)
    pl.update(window)
    ufo.update()
    events.finish(window, ufo)
