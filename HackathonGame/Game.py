import pygame
import sys
import random
import math

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
text_surface = myfont.render('Score: 0', False, (0, 0, 0))


size = Window_Width, Window_Height = 640, 480
fullWindow = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 30

score = 0

playerColor = (255, 255, 255)
enemy_color = (127, 0, 255)
GREY = (63, 63, 63)
GREEN = (0, 127, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

enemy_dead = False
enemyRadius = 10
number_of_enemies = 5
enemies_on_screen = 0
enemy_look_angle = 0
enemy_list = []
enemy_hit_box_list = []

player_dead = False
playerPos = [Window_Width//2, Window_Height//2]
playerRadius = 10
fullWindowBoarder = 10


def move(keys, event):
    if event.type == pygame.KEYDOWN or sum(keys) > 0:
        if keys[pygame.K_UP] and playerPos[1] > playerRadius + fullWindowBoarder-4:
            playerPos[1] -= 5
        if keys[pygame.K_LEFT] and playerPos[0] > (fullWindowBoarder + playerRadius)-4:
            playerPos[0] -= 5
        if keys[pygame.K_DOWN] and playerPos[1] < Window_Height - (fullWindowBoarder + playerRadius)+5:
            playerPos[1] += 5
        if keys[pygame.K_RIGHT] and playerPos[0] < Window_Width - (fullWindowBoarder + playerRadius)+5:
            playerPos[0] += 5


def attack():
    attack_box = pygame.draw.circle(fullWindow, GREEN, (playerPos[0], playerPos[1]), playerRadius+10)
    pygame.display.update()
    count = 0
    for rect in enemy_hit_box_list:
        if attack_box.colliderect(rect):
            global score
            score += 1
            global text_surface
            text_surface = myfont.render("Score: "+str(score), False, (0, 0, 0))
            enemy_hit_box_list.remove(rect)
            enemy_list.pop(count)
            global enemies_on_screen
            enemies_on_screen -= 1
        count += 1


def spawn_enemy():
    gunner = Enemy()
    gunner.create()
    enemy_list.append(gunner)
    hit_box = pygame.Rect(gunner.enemy_x_position - enemyRadius, gunner.enemy_y_position - enemyRadius,enemyRadius*2, enemyRadius*2)
    enemy_hit_box_list.append(hit_box)
    global enemies_on_screen
    enemies_on_screen += 1

def draw_enemies(player_hit_box):
    for enemy in enemy_list:
        pygame.draw.circle(fullWindow, enemy_color, (enemy.enemy_x_position, enemy.enemy_y_position), enemyRadius)
        enemy.shoot_loop()
        for projectile in enemy.projectileObjects:
            projectile.move()
            if player_hit_box.colliderect(projectile.projectile_hit_box):
                sys.exit()
            if(projectile.projectile_x_position < 0 or projectile.projectile_x_position > Window_Width or
                    projectile.projectile_y_position > Window_Height or projectile.projectile_x_position < 0):
                enemy.projectileObjects.remove(projectile)


def is_collided_with(self, object):
    return self.colliderect(object)


def game():
    while 1:
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        while enemies_on_screen < number_of_enemies:
            spawn_enemy()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.KEYDOWN or sum(keys) > 0:
            if keys[pygame.K_x]:
                attack()
        if event.type == pygame.KEYDOWN or sum(keys) > 0:
            if keys[pygame.K_SPACE]:
                enemy_list[0].shoot()
        move(keys, event)

        pygame.Surface.fill(fullWindow, GREY)
        #boarder
        pygame.draw.rect(fullWindow, (255, 255, 255), (0, 0, Window_Width, Window_Height), fullWindowBoarder)
        #player
        player_hit_box = pygame.draw.circle(fullWindow, playerColor, (playerPos[0], playerPos[1]), playerRadius)
        #score
        fullWindow.blit(text_surface, (fullWindowBoarder, fullWindowBoarder))
        #update moving stuffs
        draw_enemies(player_hit_box)
        #update frame
        pygame.display.update()


class Enemy:
    shoot_trigger = FPS
    trigger_count = 0
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
        bullet = Projectile(self.enemy_x_position - playerPos[0], self.enemy_y_position - playerPos[1], self.enemy_x_position, self.enemy_y_position)
        self.projectileObjects.append(bullet)

    def shoot_loop(self):
        if self.trigger_count > self.shoot_trigger+random.randint(0, FPS*4):
            self.shoot()
            self.trigger_count = 0
        else:
            self.trigger_count += 1


class Projectile:
    speed = 1
    projectile_hit_box = None
    projectile_x_position = 0
    projectile_y_position = 0
    x_change = None
    y_change = None
    bullet_size = 5

    def __init__(self, x_distance_to_p, y_distance_to_p, given_projectile_x_position, given_projectile_y_position):
        self. projectile_x_position = given_projectile_x_position
        self.projectile_y_position = given_projectile_y_position
        distance = (math.sqrt(x_distance_to_p**2+y_distance_to_p**2))
        self.x_change = -(x_distance_to_p / distance)*self.speed
        self.y_change = -(y_distance_to_p / distance)*self.speed


    def move(self):
        self.projectile_x_position += self.x_change
        self.projectile_y_position += self.y_change
        self.projectile_hit_box = pygame.draw.circle(fullWindow, (255, 255, 255), (math.floor(self.projectile_x_position), math.floor(self.projectile_y_position)), self.bullet_size)
        pygame.display.update()


game()
