import pygame
import random
import sys


def display_time():
    current_time = (pygame.time.get_ticks() - start_time)/1000
    time_surf = font.render(f'Time: {current_time}', False, (64, 64, 64))
    time_rect = time_surf.get_rect(center=(screen_w/2, 50))
    screen.blit(time_surf, time_rect)
    return current_time


def collided(player_mask, obs_mask, offset):
    if player_mask.overlap(obs_mask, offset):
        return True
    else:
        return False


def player_animation():
    global player_agnt


def earth_animation():
    global earth, earth_index

    earth_index += 0.05
    if (earth_index >= len(earth_ani)):
        earth_index = 0
    earth = earth_ani[int(earth_index)]


def explosion_animation(center):
    global explotion, explotion_index, explotion_rect

    explotion_rect = explotion.get_rect(center=center)

    explotion_index += 0.05
    if (explotion_index >= len(explotion_ani)):
        explotion_index = 0
    explotion = explotion_ani[int(earth_index)]


def player_move_fwd():
    global player_agnt, playerX_change
    playerX_change = 1
    player_agnt = player_agnt_move


def player_move_up():
    global player_agnt, playerY_change
    playerY_change = -2
    player_agnt = player_agnt_incl


def player_move_down():
    global player_agnt, playerY_change
    playerY_change = 2
    player_agnt = player_agnt_dcl


def player_move_slow():
    global player_agnt, playerX_change
    playerX_change = -1
    player_agnt = player_agnt_slw


def player_move_std():
    global player_agnt
    player_agnt = player_std


def respawn_player():
    global playerX_change, playerY_change, start_time, stat_velo, end_screen_counter, freeze_movement, is_collided, display_time_score

    playerX_change = 0
    playerY_change = 0
    player_move_std()
    player_agnt_rect.x = 0
    player_agnt_rect.y = random.randint(150, 450)
    earth_rect.y = random.randint(50, screen_h-256)
    stat_velo = 2
    explosion_animation((screen_w+100, screen_h+100))
    start_time = pygame.time.get_ticks()
    end_screen_counter = 0
    freeze_movement = False
    is_collided = False
    display_time_score = 0


def create_obstacle(image, cordinates):
    surface = pygame.image.load(image).convert_alpha()
    rect = surface.get_rect(topleft=(cordinates))
    mask = pygame.mask.from_surface(surface)

    return (surface, rect, mask)


def calc_offset(player_rect, obs_rect):
    offset_X = obs_rect.x - (player_rect.x)
    offset_Y = obs_rect.y - (player_rect.y)

    return (offset_X, offset_Y)


# Intialize the pygame
pygame.init()
clock = pygame.time.Clock()

# game screen size
# screen_w = pygame.display.Info().current_w
screen_w = 1200
screen_h = 600

# create the screen
screen = pygame.display.set_mode((screen_w, screen_h))
font = pygame.font.Font(pygame.font.get_default_font(), 30)

game_active = False
start_time = 0
stat_velo = 2
frame_rate = 60
# Background
background = pygame.image.load('space_bak2.png').convert()

# Obstacles
obs_plnt_1 = create_obstacle('planet.png', (screen_w*0.15, screen_h*0.2))
obs_plnt_2 = create_obstacle('planet.png', (screen_w*0.8, screen_h*0.275))
obs_plnt_3 = create_obstacle('planet_1.png', (screen_w*0.3, screen_h*0.450))
obs_plnt_4 = create_obstacle('planet_1.png', (screen_w*0.7, screen_h*0.525))
obs_ast_1 = create_obstacle('asteroid.png', (screen_w*0.5, screen_h*0.6))
obs_ast_2 = create_obstacle('asteroid.png', (screen_w*0.6, screen_h*0.1))
obs_ast_3 = create_obstacle('asteroid_1.png', (screen_w*0.25, screen_h*0.7))
obs_ast_4 = create_obstacle('asteroid_1.png', (screen_w*0.4, screen_h*0.25))

# Goal
earth_index = 0
earth1 = pygame.image.load('earth.png').convert_alpha()
earth2 = pygame.image.load('earth_flip.png').convert_alpha()
earth_ani = [earth1, earth2]
earth = earth_ani[earth_index]
earth_rect = earth.get_rect(
    center=((screen_w), random.randint(256, screen_h-256)))
earth_mask = pygame.mask.from_surface(earth)

# Player
playerX = 10
playerY = random.randint(150, 450)
playerX_change = 0
playerY_change = 0

player_std = pygame.image.load('spacecraft_std.png').convert_alpha()
player_agnt_slw = pygame.image.load('spacecraft_slow.png').convert_alpha()
player_agnt_move = pygame.image.load('spacecraft_move.png').convert_alpha()
player_agnt_incl = pygame.image.load('spacecraft_move_up.png').convert_alpha()
player_agnt_dcl = pygame.image.load('spacecraft_move_down.png').convert_alpha()

player_agnt = player_std
player_agnt_rect = player_agnt.get_rect(center=(playerX, playerY))

player_agent_mask = pygame.mask.from_surface(player_agnt)

# End Screen
player_agnt_up = pygame.image.load('spacecraft.png').convert_alpha()
player_agnt_up = pygame.transform.rotozoom(player_agnt_up, 90, 2)
player_agnt_up_rect = player_agnt_up.get_rect(center=(538, 300))
message = font.render('Press R to run', False, 'black')
message_rect = message.get_rect(bottomleft=(50, 550))
time_score = 0
game_message = ''

# Explotion
explotion_index = 0
exp1 = pygame.image.load('explotion1.png').convert_alpha()
exp1 = pygame.transform.rotozoom(exp1, 0, 3)
exp2 = pygame.image.load('explotion2.png').convert_alpha()
exp2 = pygame.transform.rotozoom(exp2, 0, 3)
exp3 = pygame.image.load('explotion3.png').convert_alpha()
exp3 = pygame.transform.rotozoom(exp3, 0, 3)
exp4 = pygame.image.load('explotion4.png').convert_alpha()
exp4 = pygame.transform.rotozoom(exp4, 0, 3)
exp5 = pygame.image.load('explotion5.png').convert_alpha()
exp5 = pygame.transform.rotozoom(exp5, 0, 3)
explotion_ani = [exp1, exp2, exp3, exp4, exp5]
explotion = explotion_ani[explotion_index]
explotion_rect = explotion.get_rect(center=(screen_w+100, screen_h+100))

end_screen_counter = 0
freeze_movement = False
is_collided = False
display_time_score = 0
# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
    screen.blit(background, (0, 0))

    # Obstacles
    screen.blit(obs_ast_1[0], obs_ast_1[1])
    screen.blit(obs_ast_2[0], obs_ast_2[1])
    screen.blit(obs_ast_3[0], obs_ast_3[1])
    screen.blit(obs_ast_4[0], obs_ast_4[1])
    screen.blit(obs_plnt_1[0], obs_plnt_1[1])
    screen.blit(obs_plnt_2[0], obs_plnt_2[1])
    screen.blit(obs_plnt_3[0], obs_plnt_3[1])
    screen.blit(obs_plnt_4[0], obs_plnt_4[1])

    # Goal - Earth
    earth_animation()
    screen.blit(earth, earth_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if game_active:

            if event.type == pygame.KEYDOWN:
                if not freeze_movement:
                    if event.key == pygame.K_LEFT:
                        player_move_slow()
                    if event.key == pygame.K_RIGHT:
                        player_move_fwd()
                    if event.key == pygame.K_UP:
                        player_move_up()
                    if event.key == pygame.K_DOWN:
                        player_move_down()
                if event.key == pygame.K_r:
                    respawn_player()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerX_change = 0
                    playerY_change = 0
                    player_move_std()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_active = True
                    respawn_player()

    if game_active:
        time_score = display_time()
        player_agnt_rect.x += playerX_change
        if player_agnt_rect.x <= 0:
            player_agnt_rect.x = 0
        elif player_agnt_rect.x >= (screen_w-64):
            player_agnt_rect.x = (screen_w-64)

        player_agnt_rect.y += playerY_change
        if player_agnt_rect.y <= 0:
            player_agnt_rect.y = 0
        elif player_agnt_rect.y >= (screen_h-64):
            player_agnt_rect.y = (screen_h-64)

        player_agnt_rect.x += stat_velo
        screen.blit(player_agnt, player_agnt_rect)
        screen.blit(explotion, explotion_rect)

        if is_collided:
            freeze_movement = True
            end_screen_counter += 1
            explosion_animation(player_agnt_rect.center)
            stat_velo = 0
            if end_screen_counter >= 30:
                game_active = False

        if not is_collided:
            if collided(player_agent_mask, obs_plnt_1[2], calc_offset(player_agnt_rect, obs_plnt_1[1])) or collided(player_agent_mask, obs_plnt_2[2], calc_offset(player_agnt_rect, obs_plnt_2[1])) or collided(player_agent_mask, obs_plnt_3[2], calc_offset(player_agnt_rect, obs_plnt_3[1])) or collided(player_agent_mask, obs_plnt_4[2], calc_offset(player_agnt_rect, obs_plnt_4[1])) or collided(player_agent_mask, obs_ast_1[2], calc_offset(player_agnt_rect, obs_ast_1[1])) or collided(player_agent_mask, obs_ast_2[2], calc_offset(player_agnt_rect, obs_ast_2[1])) or collided(player_agent_mask, obs_ast_3[2], calc_offset(player_agnt_rect, obs_ast_3[1])) or collided(player_agent_mask, obs_ast_4[2], calc_offset(player_agnt_rect, obs_ast_4[1])):
                
                display_time_score = time_score
                game_message = 'Game Over - Collision'
                is_collided = True
        if not is_collided:
            if collided(player_agent_mask, earth_mask, calc_offset(player_agnt_rect, earth_rect)):
                display_time_score = time_score
                game_message = 'Goal Reached !!'
                game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_agnt_up, player_agnt_up_rect)
        screen.blit(message, message_rect)

        time_score_surf = font.render(
            f'Time: {display_time_score}s', False, 'black')
        time_score_surf_rect = time_score_surf.get_rect(
            center=(screen_w/2, 150))

        game_msg_surf = font.render(game_message, False, 'black')
        game_msg_surf_rect = game_msg_surf.get_rect(center=(screen_w/2, 50))

        screen.blit(game_msg_surf, game_msg_surf_rect)
        if time_score > 0:
            screen.blit(time_score_surf, time_score_surf_rect)

    pygame.display.update()
    clock.tick(frame_rate)
