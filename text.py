import pygame
import graphics

def display(text):
    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render(text, True, (255, 0, 0))
    textrect = text.get_rect()
    textrect.centerx = graphics.screen.get_rect().centerx
    textrect.centery = graphics.screen.get_rect().centery
    graphics.screen.blit(text, textrect)
    pygame.display.update()