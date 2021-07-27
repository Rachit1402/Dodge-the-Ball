import sys
import random
import pygame

pygame.init()

width = 800
height: int = 600
RED = (255, 200, 0)
GREEN = (0, 200, 0 )
player_size = 50
player_pos = [width / 2, height - 2 * player_size]
enemy_size = 50
enemy_pos = [random.randint(0, width - enemy_size), 0]
clock = pygame.time.Clock()
SPEED = 10
enemy_list = [enemy_pos]

BACKGROUND_COLOR = (250, 238, 207)
Score=0
myFont = pygame.font.SysFont("momospace",35)

screen = pygame.display.set_mode((width, height))

game_over = False

def set_level(Score,SPEED):
    if Score<10:
        SPEED=4
    elif Score<20:
        SPEED=6
    elif Score<30:
        SPEED=7
    elif Score<40:
        SPEED=8
    else:
        SPEED=10
    return SPEED


def drop_enemies(enemy_list):
    delay= random.random()
    if len(enemy_list) < 10 and delay < 0.1:
        x_pos = random.randint(0, width - enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, GREEN, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))


def update_enemy_position(enemy_list,Score):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < height:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            Score += 1
    return Score


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
        return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            elif event.key == pygame. K_UP:
                y -= player_size
            elif event.key == pygame. K_DOWN:
                y += player_size

            player_pos = [x, y]

    screen.fill(BACKGROUND_COLOR)

    drop_enemies(enemy_list)
    Score= update_enemy_position(enemy_list,Score)
    SPEED=set_level(Score,SPEED)
    text = "Score" + str(Score)
    label = myFont.render(text,1,RED)
    screen.blit(label,(width-200,height-40))


    if collision_check(enemy_list,player_pos):
        game_over = True
        exit()

    draw_enemies(enemy_list)

    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)
    pygame.display.update()
