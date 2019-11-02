import pygame
import sys

pygame.init()

size = Window_Width, Window_Height = 640, 480
fullWindow = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 300

playerColor = (255, 255, 255)
GREEN = (0, 127, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
playerPos = [Window_Width//2, Window_Height//2]


def move(keys, event):
    if event.type == pygame.KEYDOWN or sum(keys) > 0:
        if keys[pygame.K_UP]:
            playerPos[1] -= 1
        if keys[pygame.K_LEFT]:
            playerPos[0] -= 1
        if keys[pygame.K_DOWN]:
            playerPos[1] += 1
        if keys[pygame.K_RIGHT]:
            playerPos[0] += 1


def attack():
    pygame.draw.circle(fullWindow, GREEN, (playerPos[0], playerPos[1]), 30)
    pygame.display.update()


def defend():
    pygame.draw.circle(fullWindow, RED, (playerPos[0], playerPos[1]), 30)
    pygame.display.update()


def game():
    while 1:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        defending = True
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
        pygame.Surface.fill(fullWindow, BLACK)
        pygame.draw.circle(fullWindow, playerColor, (playerPos[0], playerPos[1]), 20)
        pygame.display.update()

pygame.draw.rect()
game()
