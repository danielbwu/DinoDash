__author__ = 'Trenton'

import pygame
import graphics
import units
import event

graphics.init()

# - this will make a mask for the maze and make it the right size
obstacle = pygame.image.load("Easy Maze.png").convert_alpha()
obstacle = pygame.transform.scale(obstacle, (1200, 600))
obstacle_mask = pygame.mask.from_surface(obstacle)
obstacle_rect = obstacle.get_rect()

# - with will make a fossil that we can detect collision with
fossil = pygame.image.load("fossils.png").convert_alpha()
fossil_mask = pygame.mask.from_surface(fossil)
fossil_rect = fossil.get_rect()


# back = graphics.load("stars.png")
temp = graphics.load("Easy Maze.png")
graphics.background = pygame.transform.scale(temp, (1200, 600))
# graphics.load("Easy Maze.png")
# obstacle = pygame.transform.scale(graphics.background, ( 1200,  600))

george = units.George(45, 375)
george.facing = "s_down"

###
fossil = units.Fossil(1100, 150)
graphics.register(fossil)
###

graphics.register(george)


# graphics.register(george2)


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
    graphics.update()

pygame.display.quit()

print("The heaviest dinosaur was Argentinosaurus at 77 tonnes. It was the equivalent to 17 African Elephants. "
      "Argentinosaurus is a double award winner being also the longest dinosaur. It is also the largest "
      "land animal to have ever lived.")
