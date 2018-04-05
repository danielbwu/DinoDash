import pygame

foot = None
pickup = None
damage = None
arrow = None
wall = None

master_volume = 0.2


def init():
    global foot, pickup, damage, arrow, wall
    space = pygame.mixer.music.load('First_Battle.mp3')
    pygame.mixer.music.set_volume(master_volume)
    pygame.mixer.music.play(-1)

    foot = pygame.mixer.Sound('sfx_step.wav')
    foot.set_volume(master_volume)

    pickup = pygame.mixer.Sound('pickup.wav')
    pickup.set_volume(master_volume)

    arrow = pygame.mixer.Sound('arrow_hit.wav')
    arrow.set_volume(master_volume)

    wall = pygame.mixer.Sound('wall_hit.wav')
    wall.set_volume(master_volume)
