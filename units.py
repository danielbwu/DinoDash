__author__ = 'Trenton'
import pygame
import graphics
import collision
import jukebox

pygame.init()
# space = pygame.mixer.music.load('First_Battle.mp3')
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play(-1)
#
# foot = pygame.mixer.Sound('sfx_step.wav')
# foot.set_volume(0.2)
debug = False


class unit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0


class George(unit):
    def __init__(self, x, y):
        super(George, self).__init__(x, y)
        self.hp = 5
        self.walk_speed = 7.0
        self.heart = graphics.load("heart.png")
        self.spritesheet = graphics.load("trainer.png")
        self.mapping = {
            "down": [(46.75 * i, 0, 46.75, 64) for i in range(4)],
            "left": [(46.75 * i, 65, 46.75, 64) for i in range(4)],
            "right": [(46.75 * i, 128, 46.75, 64) for i in range(4)],
            "up": [(46.75 * i, 192, 46.75, 64) for i in range(4)],
            "s_down": [(0, 0, 46.75, 64) for i in range(4)],
            "s_left": [(0, 65, 46.75, 64) for i in range(4)],
            "s_right": [(0, 128, 46.75, 64) for i in range(4)],
            "s_up": [(0, 192, 46.75, 64) for i in range(4)]}

        # - with will make a back box that i will set the the location
        self.blackBox = graphics.load("black1.png").convert_alpha()
        self.blackBox = pygame.transform.scale(self.blackBox, (41, 64))
        self.box_mask = pygame.mask.from_surface(self.blackBox)
        self.facing = "down"
        self.speed = 0.3
        self.score = 0

    def update(self):
        self.frame = (self.frame + self.speed) % 4

        if self.y < 0:
            self.y = 0

        if self.y > (599 - 64):
            self.y = 599 - 64

        if self.x < 0:
            self.x = 0

        if self.x > (1200 - 46.75):
            self.x = 1200 - 46.75

    def render(self, surface):
        if debug:
            surface.blit(self.blackBox,
                         (self.x, self.y, 46.75, 64))

        surface.blit(self.spritesheet,
                     (self.x, self.y, 46.75, 64),
                     self.mapping[self.facing][int(self.frame)])

        x = 20
        for i in range(self.hp):
            surface.blit(self.heart,
                         (x, 20))
            x += 40

    def move(self, dir):
        pygame.mixer.Channel(1).play(jukebox.foot)

        if dir == "up":
            self.facing = "up"
            self.y -= self.walk_speed

        if dir == "down":
            self.facing = "down"
            self.y += self.walk_speed

        if dir == "left":
            self.facing = "left"
            self.x -= self.walk_speed

        if dir == "right":
            self.facing = "right"
            self.x += self.walk_speed

    def handler(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move("up")

            elif event.key == pygame.K_DOWN:
                self.move("down")

            elif event.key == pygame.K_LEFT:
                self.move("left")

            elif event.key == pygame.K_RIGHT:
                self.move("right")

        if event.type == pygame.KEYUP:
            pygame.mixer.Channel(1).stop()
            if event.key == pygame.K_UP:
                self.facing = "s_up"

            elif event.key == pygame.K_DOWN:
                self.facing = "s_down"

            elif event.key == pygame.K_LEFT:
                self.facing = "s_left"

            elif event.key == pygame.K_RIGHT:
                self.facing = "s_right"


class Fossil(unit):
    def __init__(self, d, type):
        super(Fossil, self).__init__(d[0], d[1])
        self.blackBox = graphics.load("black1.png").convert_alpha()
        self.blackBox = pygame.transform.scale(self.blackBox, (45, 45))
        self.box_mask = pygame.mask.from_surface(self.blackBox)
        self.type = type
        self.spritesheet = graphics.load("fossils.png")
        self.spritesheet = pygame.transform.scale(self.spritesheet, (125, 65))
        self.mapping = {
            0: (0, 10, 41.6, 65),
            1: (45, 12, 41.6, 40),
            2: (83.3, 20, 41.6, 40)
        }
        graphics.register(self)

    def render(self, surface):
        if debug:
            surface.blit(self.blackBox,
                         (self.x, self.y, 46.75, 64),
                         (0, 0, 45, 45))
        surface.blit(self.spritesheet,
                     (self.x, self.y),
                     self.mapping[self.type])

    def destroy(self):
        collision.remove_fossil(self)
        graphics.remove(self)


class Arrow(unit):
    def __init__(self, x, y, dir):
        super(Arrow, self).__init__(x, y)
        self.dir = dir
        self.move_speed = 14.0
        self.spritesheet = graphics.load("arrow1.png").convert_alpha()
        self.spritesheet = pygame.transform.scale(self.spritesheet, (84, 24))
        if dir == 1:
            self.spritesheet = pygame.transform.flip(self.spritesheet, True, False)
        self.box_mask = pygame.mask.from_surface(self.spritesheet)
        graphics.register(self)

    def render(self, surface):
        surface.blit(self.spritesheet,
                     (self.x, self.y))

    def update(self):
        if self.dir == 0:
            self.x -= self.move_speed
        else:
            self.x += self.move_speed

        if self.x < 0 or self.x > 1200:
            self.destroy()

    def destroy(self):
        collision.remove_arrow(self)
        graphics.remove(self)
