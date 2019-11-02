import pygame
import sys
import random

pygame.init()

size = Window_Width, Window_Height = 640, 480
fullWindow = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 300

playerColor = (255, 255, 255)
GREY = (63, 63, 63)
GREEN = (0, 127, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

number_of_enemies = 5
enemies_on_screen = 0
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
    enemy_x = random.randint(0, Window_Width)
    enemy_y = random.randint(0, Window_Width)


def updateGame():
    pass


def game():
    while 1:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        defending = True

        #while enemies_on_screen < number_of_enemies:
        #    spawn_enemy()

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
        #update frame
        pygame.display.update()
        #update moving stuffs


game()
