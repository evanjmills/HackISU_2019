import pygame

speed = None
angle = None
hit_box = pygame.draw.circle()


def __init__(given_speed, given_angle):
    global speed
    global angle
    speed = given_speed
    angle = given_angle
