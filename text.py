import pygame
import graphics


def display_score(text):
    basicfont = pygame.font.SysFont(None, 32)
    text = basicfont.render(text, True, (255, 0, 0))
    textrect = text.get_rect()
    textrect.centerx = 68
    textrect.centery = 65
    graphics.screen.blit(text, textrect)
    pygame.display.update()
