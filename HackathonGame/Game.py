import pygame
import sys
import _thread
import time
import asyncio
import threading
import random
import math

pygame.init()

size = Window_Width, Window_Height = 640, 480
fullWindow = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 300

playerColor = (255, 255, 255)
enemy_color = (127, 0, 255)
GREY = (63, 63, 63)
GREEN = (0, 127, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

enemy_dead = False
enemyRadius = 20
number_of_enemies = 1
enemies_on_screen = 0
enemy_look_angle = 0
enemy_list = []

playerPos = [Window_Width//2, Window_Height//2]
playerRadius = 20
fullWindowBoarder = 10


def move(keys, event):
    if event.type == pygame.KEYDOWN or sum(keys) > 0:
        if keys[pygame.K_UP] and playerPos[1] > playerRadius + fullWindowBoarder-4:
            playerPos[1] -= 1
        if keys[pygame.K_LEFT] and playerPos[0] > (fullWindowBoarder + playerRadius)-4:
            playerPos[0] -= 1
        if keys[pygame.K_DOWN] and playerPos[1] < Window_Height - (fullWindowBoarder + playerRadius)+5:
            playerPos[1] += 1
        if keys[pygame.K_RIGHT] and playerPos[0] < Window_Width - (fullWindowBoarder + playerRadius)+5:
            playerPos[0] += 1


def attack():
    pygame.draw.circle(fullWindow, GREEN, (playerPos[0], playerPos[1]), playerRadius+10)
    pygame.display.update()


def defend():
    pygame.draw.circle(fullWindow, RED, (playerPos[0], playerPos[1]), playerRadius+10)
    pygame.display.update()


def spawn_enemy():
    gunner = Enemy()
    gunner.create()
    enemy_list.append(gunner)
    global enemies_on_screen
    enemies_on_screen += 1

def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.circle(fullWindow, enemy_color, (enemy.enemy_x_position, enemy.enemy_y_position), enemyRadius)
        for projectile in enemy.projectileObjects:
            projectile.move()
            if(projectile.projectile_x_position < 0 or projectile.projectile_x_position > Window_Width or projectile.projectile_y_position > Window_Height or projectile.projectile_x_position < 0):
                enemy.projectileObjects.remove(projectile)


def game():
    while 1:
        keys = pygame.key.get_pressed()
        clock.tick()
        #print(clock.get_fps())
        defending = True
        while enemies_on_screen < number_of_enemies:
            spawn_enemy()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.KEYDOWN or sum(keys) > 0:
            if keys[pygame.K_x]:
                attack()
        if event.type == pygame.KEYDOWN or sum(keys) > 0:
            if keys[pygame.K_z]:
                defend()
                defending = False
        if event.type == pygame.KEYDOWN or sum(keys) > 0:
            if keys[pygame.K_SPACE]:
                enemy_list[0].shoot()
        if defending:
            move(keys, event)

        pygame.Surface.fill(fullWindow, GREY)
        #boarder
        pygame.draw.rect(fullWindow, (255, 255, 255), (0, 0, Window_Width, Window_Height), fullWindowBoarder)
        #player
        pygame.draw.circle(fullWindow, playerColor, (playerPos[0], playerPos[1]), playerRadius)
        #update moving stuffs
        draw_enemies()
        #update frame
        pygame.display.update()


class Enemy:
    time_elapsed = 0
    enemy_x_position = Window_Width//2
    enemy_y_position = Window_Height//2
    projectileObjects = []

    def create(self):
        while (self.enemy_x_position < Window_Width//2+75 and self.enemy_x_position > Window_Width//2-75) \
                and (self.enemy_y_position < Window_Height//2+75 and self.enemy_y_position > Window_Height//2-75):
            self.enemy_x_position = random.randint((fullWindowBoarder + playerRadius)-4,
                                                   Window_Width - (fullWindowBoarder + playerRadius))
            self.enemy_y_position = random.randint(playerRadius + fullWindowBoarder-4,
                                                   Window_Height - (fullWindowBoarder + playerRadius)+5)
        pygame.draw.circle(fullWindow, enemy_color, (self.enemy_x_position, self.enemy_y_position), enemyRadius)
        self.shoot_loop()

    def draw_enemy(self):
        pygame.draw.circle(fullWindow, enemy_color, (self.enemy_x_position, self.enemy_y_position), enemyRadius)
        pygame.display.update()

    def shoot(self):
        bullet = Projectile(5, self.enemy_x_position - playerPos[0], self.enemy_y_position - playerPos[1], self.enemy_x_position, self.enemy_y_position)
        self.projectileObjects.append(bullet)

    def shoot_loop(self):
        if clock.get_time() > 10:
            self.shoot()
        else:
            self.time_elapsed += clock.get_time()


class Projectile:
    speed = None
    projectile_x_position = 0
    projectile_y_position = 0
    x_change = None
    y_change = None
    bullet_size = 10

    def __init__(self, given_speed, x_distance_to_p, y_distance_to_p, given_projectile_x_position, given_projectile_y_position):
        self. projectile_x_position = given_projectile_x_position
        self.projectile_y_position = given_projectile_y_position
        self.speed = given_speed
        distance = (math.sqrt(math.pow(x_distance_to_p, 2)+math.pow(x_distance_to_p, 2)))
        self.x_change = -(x_distance_to_p / distance)
        self.y_change = -(y_distance_to_p / distance)

    def move(self):
        self.projectile_x_position += self.x_change*self.speed
        self.projectile_y_position += self.y_change*self.speed
        pygame.draw.circle(fullWindow, (255, 255, 255), (math.floor(self.projectile_x_position), math.floor(self.projectile_y_position)), self.bullet_size)
        pygame.display.update()


game()
