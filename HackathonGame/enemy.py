import pygame
import random
import projectile
import threading

full_window = None
position = [0, 0]
color = (127, 0, 255)
enemyRadius = 20
hit_box = None
look_angle = 0
shoot_Speed = 5
shoot_timer = 10


def __init__(given_full_window, screen_width, screen_height):
    global hit_box
    global full_window
    full_window = given_full_window
    position[0] = random.randint(0, screen_width)
    position[1] = random.randint(0, screen_height)
    hit_box = pygame.draw.circle(full_window, color, (position[0], position[1]), enemyRadius)


def shoot():
    projectile(full_window, look_angle)


def enemy_loop():
    count = 0
    while 1:
        count += 1
        if count % 100 == 0:
            shoot()
