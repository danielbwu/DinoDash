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

###
# fossil = units.Fossil(590, 45, 0)
# fossil1 = units.Fossil(590, 160, 1)
# fossil2 = units.Fossil(720, 160, 2)
# graphics.register(fossil)
# graphics.register(fossil1)
# graphics.register(fossil2)
# collision.register_fossil(fossil)
# collision.register_fossil(fossil1)
# collision.register_fossil(fossil2)
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
