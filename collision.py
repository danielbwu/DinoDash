import pygame
import units
import graphics
import text
from random import randint

player = None  # type: units.George
map = None
fossils = []   # type: units.Fossil
arrows = []    # type: units.Arrow
spawn_chance = 7


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


def remove_fossil(f):
    global fossils
    if f in fossils:
        fossils.remove(f)


def register_arrow(a):
    global arrows
    if a not in arrows:
        arrows.append(a)


def remove_arrow(a):
    global arrows
    if a in arrows:
        arrows.remove(a)


def update():
    # Map collision
    if map.overlap(player.box_mask, (int(player.x), int(player.y))):
        player.x = 45
        player.y = 375
        # text.display("Hit wall")

    # Fossils
    for f in fossils:
        if player_collision(f):
            text.display("Fossil found!")

    # Arrows
    for a in arrows:
        a.update()
        if player_collision(a):
            text.display("Arrow hit!")
            player.x = 45
            player.y = 375


def player_collision(obj):
    return obj.box_mask.overlap(player.box_mask,
                               (int(player.x - obj.x),
                                int(player.y - obj.y))
                               )


def arrow_gen():
    chance = randint(0, 1000)
    if chance <= spawn_chance:
        a = units.Arrow(1200, randint(10, 590))
        register_arrow(a)
