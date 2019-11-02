import pygame
import sys
import _thread
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
number_of_enemies = 5
enemies_on_screen = 0
enemy_look_angle = 0
enemy_list = []

playerPos = [Window_Width//2, Window_Height//2]
playerRadius = 20
fullWindowBoarder = 10
projectileObject = []


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
    gunner.__init__()
    enemy_list.append(gunner)
    global enemies_on_screen
    enemies_on_screen += 1


def draw_enemies():
    for enemy in enemy_list:
        pygame.draw.circle(fullWindow, enemy_color, (enemy.enemy_x_position, enemy.enemy_y_position), enemyRadius)


def game():
    while 1:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
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
    enemy_x_position = Window_Width//2
    enemy_y_position = Window_Height//2

    def __init__(self):
        while (self.enemy_x_position < Window_Width//2+75 and self.enemy_x_position > Window_Width//2-75) \
                and (self.enemy_y_position < Window_Height//2+75 and self.enemy_y_position > Window_Height//2-75):
            self.enemy_x_position = random.randint((fullWindowBoarder + playerRadius)-4,
                                                   Window_Width - (fullWindowBoarder + playerRadius))
            self.enemy_y_position = random.randint(playerRadius + fullWindowBoarder-4,
                                                   Window_Height - (fullWindowBoarder + playerRadius)+5)
        pygame.draw.circle(fullWindow, enemy_color, (self.enemy_x_position, self.enemy_y_position), enemyRadius)

    def draw_enemy(self):
        pygame.draw.circle(fullWindow, enemy_color, (self.enemy_x_position, self.enemy_y_position), enemyRadius)
        pygame.display.update()

    def shoot(self):
        bullet = Projectile(fullWindow, enemy_look_angle)
        _thread.start_new_thread(bullet.move())

    def enemy_loop(self):
        count = 0
        while 1:
            count += 1
            if count % 1000 == 0:
                self.shoot()


class Projectile:
    speed = None
    full_window = None
    position = []
    x_change = None
    y_change = None
    bullet_size = 10

    def __init__(self, given_full_window, given_speed, x_distance_to_p, y_distance_to_p, given_position):
        global speed
        global x_change
        global y_change
        global full_window
        global position
        position = given_position
        full_window = given_full_window
        speed = given_speed
        angle = math.degrees(math.atan(y_distance_to_p / x_distance_to_p))
        x_change = math.cos(angle)
        y_change = math.sin(angle)

    def move(self):
        global bullet_size
        count = 0
        while 1:
            count += 1
            position[0] += x_change
            position[1] += y_change
            pygame.draw.circle(full_window, (255, 255, 255), position, bullet_size)
            pygame.display.update()
            if count > 5000:
                break;

game()
