__author__ = 'Trenton'

import pygame
import graphics
import units
import event
import collision
import random

graphics.init()

# - this will make a mask for the maze and make it the right size
obstacle = pygame.image.load("Easy Maze.png").convert_alpha()
obstacle = pygame.transform.scale(obstacle, (1200, 600))
obstacle_mask = pygame.mask.from_surface(obstacle)
obstacle_rect = obstacle.get_rect()
collision.set_map(obstacle_mask)
graphics.background = obstacle

george = units.George(45, 375)
george.facing = "s_down"
collision.set_player(george)
graphics.register(george)

###
fossil = units.Fossil(1100, 150, 0)
fossil1 = units.Fossil(200, 200, 1)
fossil2 = units.Fossil(500, 150, 2)
graphics.register(fossil)
graphics.register(fossil1)
graphics.register(fossil2)
collision.register_fossil(fossil)
collision.register_fossil(fossil1)
collision.register_fossil(fossil2)
###

# arrow = units.Arrow(1000, 100)
# graphics.register(arrow)
# collision.register_arrow(arrow)


def quit(e):
    global run
    if e.type == pygame.QUIT:
        run = False
    elif e.type == pygame.KEYUP:
        if (e.key == pygame.K_F4) and (e.mod and pygame.KMOD_ALT):
            run = False


event.register(george.handler)
event.register(quit)

clock = pygame.time.Clock()
run = True
frame = 0

while run:
    clock.tick(30)
    event.update()
    george.update()
    collision.update()
    collision.arrow_gen()
    graphics.update()


pygame.display.quit()

print("The heaviest dinosaur was Argentinosaurus at 77 tonnes. It was the equivalent to 17 African Elephants. "
      "Argentinosaurus is a double award winner being also the longest dinosaur. It is also the largest "
      "land animal to have ever lived.")
