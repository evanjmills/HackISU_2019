import pygame
import sys

pygame.init()
size = Window_Width, Window_Height = 640, 480
fullWindow = pygame.display.set_mode(size)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()