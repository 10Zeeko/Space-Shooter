from ..game_config.cons import *
from . import bullet
from ..game_config.debug import *
from ..game_systems.input_manager import *
from ..game_systems.effects_manager import *

def create_player():
    player = {
        'right': PLAYER_RIGHT,
        'left': PLAYER_LEFT,
        'idle': PLAYER_IDLE,
        'lives': 3,
        'score': 0,
        'bullets':[],
        'bullet_cooldown': 0,
        'x':400-50,
        'y':800-76,
        'invincible': False,
        'speed_boost': False,
        'shield': False,
        'double_laser': False
    }
    player['sprites'] = player['idle']
    player['hitbox'] = pygame.Rect(player['x'] + 35, player['y'] + 5, 29, 95)
    player['pick_hitbox'] = PLAYER_IDLE.get_rect(topleft=(player['x'], player['y']))
    return player

def draw_player(screen, player):
    sprite = player['sprites']
    square = sprite.get_rect().move(player['x'], player['y'])
    screen.blit(sprite, square)

    # Draw player hitbox for debugging
    if get_debug_toggle():
        pygame.draw.rect(screen, (255, 0, 0), player['hitbox'], 2)  # Red rectangle
        pygame.draw.rect(screen, (0, 255, 100), player['pick_hitbox'], 2)  # Green rectangle

def move_player(player, delta, bullets):
    global debug_toggle
    moved = False
    # Increase the velocity if the speed boost power-up is active
    vel = int(PLAYER_VEL * delta * (1.5 if player.get('speed_boost', False) else 1))
    keys = pygame.key.get_pressed()
    if left_input(keys) and player['x']>0:
        player['x'] = max(player['x'] - vel, 0)
        player['sprites'] = player['left']
        moved = True
    if right_input(keys) and player['x']< WINDOW_SIZE_X -100:
        player['x']=min(player['x']+vel, WINDOW_SIZE_X-50)
        player['sprites']=player['right']
        moved=True
    if shoot_input(keys):
        now = pygame.time.get_ticks()
        if now - player['bullet_cooldown'] >= BULLET_COOLDOWN:
            player['bullet_cooldown'] = pygame.time.get_ticks()
            player_bullet = bullet.create_bullet(player['x'] + 45.5, player['y'] - 18.5, 0)
            player_bullet['angle'] = 0
            # If the double laser power-up is active, create an additional bullet
            if player.get('double_laser', False):
                player_bullet['x'] = player_bullet['x'] - 3.0
                player_bullet2 = bullet.create_bullet(player['x'] + 48.5, player['y'] - 18.5, 0)
                player_bullet2['angle'] = 0
                bullets.append(player_bullet2)
            bullets.append(player_bullet)
            
    if debug_input(keys):
        debug_value = not get_debug_toggle()
        set_debug_toggle(debug_value)
    if not moved:
        player['sprites'] = player['idle']

    # Update the hitbox position to move with the player
    player['hitbox'].topleft = (player['x'] + 35, player['y'] + 5)
    player['pick_hitbox'].topleft = (player['x'], player['y'])

def player_update(player, delta, screen, enemies, bullets):
    move_player(player, delta, bullets)
    update_game_object(player)
    draw_player(screen, player)
    check_colliosins(player, enemies)

    return True # Player is still alive

def check_colliosins(player, enemies):
    # Check player collisions with enemies
    player_rect = player['hitbox']
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 93, 84)
        if player_rect.colliderect(enemy_rect):
            player['lives'] -= 1
            enemies.remove(enemy)
            if player['lives'] == 0:
                break  # Player has no lives left

def player_hit(player):
    player['lives'] -= 1
    blink(player, (90, 30, 30), 2, 150)
    if player['lives'] == 0:
        print("Game Over")  # Player has no lives left

def add_points_to_score(player, points):
    player['score'] += points

def activate_power_up(player, power_up):
    power_up_type = power_up['power_up_type']
    if power_up_type == 0:  # Invincibility
        player['invincible'] = True
        pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
    elif power_up_type == 1:  # Speed boost
        player['speed_boost'] = True
        pygame.time.set_timer(pygame.USEREVENT + 2, 6000)
    elif power_up_type == 2:  # Shield
        player['shield'] = True
    elif power_up_type == 3:  # Double laser
        player['double_laser'] = True
        pygame.time.set_timer(pygame.USEREVENT + 3, 4000)