import pygame
import units
import graphics
import text

player = None  # type: George
map = None
fossils = []
arrows = []
fossil = None


def set_player(p):
    global player
    player = p


def set_map(m):
    global map
    map = m


def register_fossil(f):
    global fossils
    if f not in fossils:
        fossils.append(f)


def update():
    if map.overlap(player.box_mask, (int(player.x), int(player.y))):
        player.x = 45
        player.y = 375
        # text.display("Hit wall")

    if fossil.box_mask.overlap(player.box_mask,
                               (int(player.x - fossil.x),
                                int(player.y - fossil.y))
                               ):
        text.display("Fossil found!")
