import pygame
import sys
import random
import math
import neat
import os

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

root_two = math.sqrt(2)
slopes = [(1, 0), (root_two / 2, root_two / 2), (0, 1), (-1 * root_two, root_two), (-1, 0), (-1 * root_two, -1 *
                                                                        root_two), (0, -1), (root_two, -1 * root_two)]


# def move(keys, event):
    # if event.type == pygame.KEYDOWN or sum(keys) > 0:
    #     if keys[pygame.K_UP] and playerPos[1] > playerRadius + fullWindowBoarder-4:
    #         playerPos[1] -= 5
    #     if keys[pygame.K_LEFT] and playerPos[0] > (fullWindowBoarder + playerRadius)-4:
    #         playerPos[0] -= 5
    #     if keys[pygame.K_DOWN] and playerPos[1] < Window_Height - (fullWindowBoarder + playerRadius)+5:
    #         playerPos[1] += 5
    #     if keys[pygame.K_RIGHT] and playerPos[0] < Window_Width - (fullWindowBoarder + playerRadius)+5:
    #         playerPos[0] += 5
def move(output, genome):
    if output[0] >= 0.5 and playerPos[1] > playerRadius + fullWindowBoarder-4:
        playerPos[1] -= 5
    if output[1] >= 0.5 and playerPos[0] > (fullWindowBoarder + playerRadius)-4:
        playerPos[0] -= 5
    if output[2] >= 0.5 and playerPos[1] < Window_Height - (fullWindowBoarder + playerRadius)+5:
        playerPos[1] += 5
    if output[3] >= 0.5 and playerPos[0] < Window_Width - (fullWindowBoarder + playerRadius)+5:
        playerPos[0] += 5

    genome.fitness += 0.1


def attack(genome):
    attack_box = pygame.draw.circle(fullWindow, GREEN, (playerPos[0], playerPos[1]), playerRadius+10)
    pygame.display.update()
    count = 0
    for rect in enemy_hit_box_list:
        if attack_box.colliderect(rect):
            global score
            score += 10
            global text_surface
            text_surface = myfont.render("Score: "+str(score), False, (0, 0, 0))
            enemy_hit_box_list.remove(rect)
            enemy_list.pop(count)
            global enemies_on_screen
            enemies_on_screen -= 1

            genome.fitness += 10
        count += 1


def spawn_enemy():
    gunner = Enemy()
    gunner.create()
    enemy_list.append(gunner)
    hit_box = pygame.Rect(gunner.enemy_x_position - enemyRadius, gunner.enemy_y_position - enemyRadius,enemyRadius*2, enemyRadius*2)
    enemy_hit_box_list.append(hit_box)
    global enemies_on_screen
    enemies_on_screen += 1


def draw_enemies(player_hit_box, genome):
    for enemy in enemy_list:
        pygame.draw.circle(fullWindow, enemy_color, (enemy.enemy_x_position, enemy.enemy_y_position), enemyRadius)
        enemy.shoot_loop()
        for projectile in enemy.projectileObjects:
            projectile.move()
            if player_hit_box.colliderect(projectile.projectile_hit_box):
                genome.fitness -= 10
                print("end")
                global cont
                cont = False
                # sys.exit()
            if(projectile.projectile_x_position < 0 or projectile.projectile_x_position > Window_Width or
                    projectile.projectile_y_position > Window_Height or projectile.projectile_x_position < 0):
                enemy.projectileObjects.remove(projectile)

    return False


def is_collided_with(self, object):
    return self.colliderect(object)


def vision():
    enemy = False
    projectile = False
    wall = False
    for idx, slope in enumerate(slopes):
        nodes = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        xslope = slope[0]
        yslope = slope[1]
        x = playerPos[0]
        y = playerPos[1]
        distance = 0
        while not enemy and not projectile and not wall:
            for enm in enemy_list:
                if enm.enemy_x_position <= x and enm.enemy_x_position + 2*enemyRadius >= x and enm.enemy_y_position < y \
                        and enm.enemy_y_position + 2*enemyRadius:
                    enemy = True
                    nodes[2*idx] = distance
                    break
                for proj in enm.projectileObjects:
                    if(proj.projectile_x_position < x and proj.projectile_x_position + 2*proj.bullet_size and
                            proj.projectile_y_position < y and proj.projectile_y_position + 2*proj.bullet_size):
                        projectile = True
                        nodes[2*idx + 1] = distance
                        break
                if projectile:
                    break
                if playerRadius + fullWindowBoarder - 4 >= y or Window_Height - (
                        fullWindowBoarder + playerRadius) + 5 <= y or \
                        (fullWindowBoarder + playerRadius) - 4 >= x or Window_Width - (
                        fullWindowBoarder + playerRadius) + 5 <= x:
                    wall = True

                distance += 1
                x += xslope
                y += yslope



    return nodes


def game(genome, net):
    counter = 0
    global cont
    cont = True
    while cont:
        if(counter % FPS == 0):
            global score
            global text_surface
            score += 1
            text_surface = myfont.render("Score: " + str(score), False, (0, 0, 0))
        keys = pygame.key.get_pressed()
        clock.tick(FPS)
        while enemies_on_screen < number_of_enemies:
            spawn_enemy()

        pygame.Surface.fill(fullWindow, GREY)
        # boarder
        pygame.draw.rect(fullWindow, (255, 255, 255), (0, 0, Window_Width, Window_Height), fullWindowBoarder)
        # player
        player_hit_box = pygame.draw.circle(fullWindow, playerColor, (playerPos[0], playerPos[1]), playerRadius)
        # score
        fullWindow.blit(text_surface, (fullWindowBoarder, fullWindowBoarder))
        # update moving stuffs
        draw_enemies(player_hit_box, genome)
        # update frame
        pygame.display.update()

        inputs = vision()
        outputs = net.activate(inputs)

        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # if event.type == pygame.KEYDOWN or sum(keys) > 0:
        #     if keys[pygame.K_x]:
        #         attack(genome)
        # if event.type == pygame.KEYDOWN or sum(keys) > 0:
        #     if keys[pygame.K_SPACE]:
        #         enemy_list[0].shoot()

        if outputs[4] >= 0.5:
            attack(genome)

        move(outputs, genome)

        counter += 1

        # move(keys, event, genome)



class Enemy:
    shoot_trigger = int(FPS)
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


def eval_genomes(genomes, config):
    nets = []
    ge = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        ge.append(genome)

    for x, net in enumerate(nets):
        game(ge[x], net)


def run(config_path):
    # load config file
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    # create the population
    p = neat.Population(config)

    # add reporters
    # p.add_reporter(neat.StdOutReporter)
    # p.add_reporter(neat.StatisticsReporter)
    # p.add_reporter(neat.checkpoint(5))

    winner = p.run(eval_genomes, 100)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
