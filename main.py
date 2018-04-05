__author__ = 'Trenton'

import pygame
import graphics
import units
import event
import collision
import jukebox
import text


pygame.init()
graphics.init()
jukebox.init()

texture = pygame.image.load("dungeon_texture.png")
texture = pygame.transform.scale(texture, (1200, 600))
graphics.background = texture
# - this will make a mask for the maze and make it the right size
obstacle = pygame.image.load("Easy Maze.png").convert_alpha()
obstacle = pygame.transform.scale(obstacle, (1200, 600))
obstacle_mask = pygame.mask.from_surface(obstacle)
obstacle_rect = obstacle.get_rect()
collision.set_map(obstacle_mask)
graphics.dungeon = obstacle

george = units.George(45, 375)
george.facing = "s_down"
collision.set_player(george)
graphics.register(george)

collision.fossil_gen()


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

while run and george.hp > 0:
    clock.tick(30)
    event.update()
    george.update()
    collision.update()
    collision.arrow_gen()
    graphics.update()
    text.display_score("Score: " + str(george.score))


pygame.display.quit()

print("Score: " + str(george.score))
print("The heaviest dinosaur was Argentinosaurus at 77 tonnes. It was the equivalent to 17 African Elephants. "
      "Argentinosaurus is a double award winner being also the longest dinosaur. It is also the largest "
      "land animal to have ever lived.")
