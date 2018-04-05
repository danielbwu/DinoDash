import pygame
import units
import graphics
import text
import jukebox
from random import randint

player = None  # type: units.George
map = None
fossils = []   # type: units.Fossil
arrows = []    # type: units.Arrow
spawn_chance = 10


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
        pygame.mixer.Channel(2).play(jukebox.wall)
        player.x = 45
        player.y = 375

    # Fossils
    for f in fossils:
        if player_collision(f):
            pygame.mixer.Channel(3).play(jukebox.pickup)
            player.score += 1
            f.destroy()
            fossil_gen()

    # Arrows
    for a in arrows:
        a.update()
        if player_collision(a):
            pygame.mixer.Channel(3).play(jukebox.arrow)
            player.hp -= 1
            a.destroy()


def player_collision(obj):
    return obj.box_mask.overlap(player.box_mask,
                               (int(player.x - obj.x),
                                int(player.y - obj.y))
                               )


def arrow_gen():
    chance = randint(0, 1000)
    if chance <= spawn_chance:
        a = units.Arrow(1200 if player.x < 600 else 0,
                        int(player.y + randint(-20, 20)),
                        0 if player.x < 600 else 1)
        register_arrow(a)


def fossil_gen():
    mapping = {
        0: (30, 520),
        1: (310, 300),
        2: (590, 45),
        3: (590, 160),
        4: (720, 160),
        5: (1110, 160)
    }

    f = units.Fossil(mapping[randint(0, 5)], randint(0, 2))
    register_fossil(f)
