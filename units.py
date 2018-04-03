__author__ = 'Trenton'
import pygame
import graphics

pygame.init()
space = pygame.mixer.music.load('Spacetime.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

foot = pygame.mixer.Sound('Footsteps2.wav')
foot.set_volume(0.3)
debug = False

class unit(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = 0.0


class George(unit):
    def __init__(self, x, y):
        super(George, self).__init__(x, y)
        self.walk_speed = 5.0
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
        self.blackBox = pygame.image.load("black1.png").convert_alpha()
        self.blackBox =  pygame.transform.scale(self.blackBox, (46 , 64 ))
        self.box_mask = pygame.mask.from_surface(self.blackBox)
        # self.box_rect = self.blackBox.get_rect()
        # self.box_rect.center = (self.x, self.y)
        self.hitbox = pygame.Rect(self.x - 23, self.y - 32, 46, 64)
        # self.hitbox.width = 46
        # self.hitbox.height = 64
        self.hitbox.center = (self.x, self.y)
        self.facing = "down"
        self.speed = 0.3

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
                        (self.x, self.y, 46.75, 64),
                        (0, 0, 46.75, 64))

        surface.blit(self.spritesheet,
                     (self.x, self.y, 46.75, 64),
                     self.mapping[self.facing][int(self.frame)])


    def move(self, dir):
        foot.play()

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
            foot.play()

            if event.key == pygame.K_UP:
                self.move("up")

            elif event.key == pygame.K_DOWN:
                self.move("down")

            elif event.key == pygame.K_LEFT:
                self.move("left")

            elif event.key == pygame.K_RIGHT:
                self.move("right")

        if event.type == pygame.KEYUP:
            foot.stop()
            if event.key == pygame.K_UP:
                self.facing = "s_up"

            elif event.key == pygame.K_DOWN:
                self.facing = "s_down"

            elif event.key == pygame.K_LEFT:
                self.facing = "s_left"

            elif event.key == pygame.K_RIGHT:
                self.facing = "s_right"



class Fossil(unit):
    def __init__(self, x, y, type):
        super(Fossil, self).__init__(x, y)
        self.blackBox = pygame.image.load("black1.png").convert_alpha()
        self.blackBox = pygame.transform.scale(self.blackBox, (45, 45))
        self.box_mask = pygame.mask.from_surface(self.blackBox)
        self.type = type
        self.spritesheet = graphics.load("fossils.png")
        self.spritesheet = pygame.transform.scale(self.spritesheet, (125, 65))
        self.mapping = {
            0: (0, 0, 41.6, 65),
            1: (41.6, 0, 83.3, 65),
            2: (83.3, 0, 125, 65)
        }

    def render(self, surface):
        if debug:
            surface.blit(self.blackBox,
                        (self.x, self.y, 46.75, 64),
                        (0, 0, 45, 45))
        surface.blit(self.spritesheet,
                        (self.x, self.y, 46.75, 64),
                         self.mapping[self.type])


class Arrow(unit):
    def __init__(self, x, y):
        super(Arrow, self).init(x, y)
        self.spritesheet = graphics.load("arrow1.png")
        self.blackBox = pygame.image.load("black1.png").convert_alpha()
        self.blackBox = pygame.transform.scale(self.blackBox, (46, 64))
        self.box_mask = pygame.mask.from_surface(self.blackBox)

    def render(self, surface):
        if debug:
            surface.blit(self.blackBox,
                        (self.x, self.y, 46.75, 64),
                        (0, 0, 45, 45))
        surface.blit(self.spritesheet,
                        (self.x, self.y, 46.75, 64),
                         self.mapping[self.type])