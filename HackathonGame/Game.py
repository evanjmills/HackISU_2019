import pygame
import sys

pygame.init()

size = Window_Width, Window_Height = 640, 480
fullWindow = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 144

playerColor = (255, 255, 255)
BLACK = (0, 0, 0)
playerPos = [Window_Width//2, Window_Height//2]
player = pygame.display.set_mode(size)


def move(keys, event):
    if event.type == pygame.KEYDOWN or sum(keys) > 0:
        if keys[pygame.K_w]:
            playerPos[1] -= 1
        if keys[pygame.K_a]:
            playerPos[0] -= 1
        if keys[pygame.K_s]:
            playerPos[1] += 1
        if keys[pygame.K_d]:
            playerPos[0] += 1

def attack():
    pygame.draw.circle(fullWindow, playerColor, (playerPos[0], playerPos[1]), 30, 5)

def game():
    while 1:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        move(keys, event)
        attack()

        pygame.Surface.fill(fullWindow, BLACK)
        pygame.draw.circle(fullWindow, playerColor, (playerPos[0], playerPos[1]), 20)
        pygame.display.update()


game()
