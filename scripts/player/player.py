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
        'alive': True,
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
    player['shield_sprites'] = SHIELD_SPRITE
    return player

def draw_player(screen, player):
    sprite = player['sprites']
    square = sprite.get_rect().move(player['x'], player['y'])
    screen.blit(sprite, square)

    # Draw the shield if it's active
    if player['shield']:
        shield_sprite = player['shield_sprite']
        shield_square = shield_sprite.get_rect().move(player['x'] - 20, player['y'] - 20)
        screen.blit(shield_sprite, shield_square)

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
            LASER_SOUND.play()
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

def player_update(player, delta, screen, bullets):
    move_player(player, delta, bullets)
    update_effects_game_object(player)
    update_shield(player)
    draw_player(screen, player)
    return player['alive'] # Player is still alive

def player_hit(player):
    player['lives'] -= 1
    blink(player, (90, 30, 30), 2, 150)
    if player['lives'] == 0:
        print("Game Over")  # Player has no lives left

def add_points_to_score(player, points):
    player['score'] += points

def activate_power_up(player, power_up):
    power_up_type = power_up['power_up_type']
    POWER_UP_PICK_SOUND.play()
    if power_up_type == 0:  # Invincibility
        player['invincible'] = True
        blink(player, (20, 90, 90), 3, 1000)
        pygame.time.set_timer(pygame.USEREVENT + 1, 3000)
    elif power_up_type == 1:  # Speed boost
        player['speed_boost'] = True
        pygame.time.set_timer(pygame.USEREVENT + 2, 6000)
    elif power_up_type == 2:  # Shield
        player['shield'] = True
        add_shield(player)
    elif power_up_type == 3:  # Double laser
        player['double_laser'] = True
        pygame.time.set_timer(pygame.USEREVENT + 3, 4000)

def add_shield(player):
    player['shield'] = True
    player['shield_sprite'] = player['shield_sprites'][0]
    player['shield_start_time'] = pygame.time.get_ticks()
    player['shield_animation_done'] = False

def update_shield(player):
    # If the shield is active, update the shield sprite
    if player['shield'] and not player['shield_animation_done']:
        elapsed_time = pygame.time.get_ticks() - player['shield_start_time']
        sprite_index = int((elapsed_time / 1000) * len(player['shield_sprites']))
        if sprite_index < len(player['shield_sprites']):
            player['shield_sprite'] = player['shield_sprites'][sprite_index]
        else:
            # If the last sprite has been displayed, stop the animation
            player['shield_animation_done'] = True
            player['shield_sprite'] = player['shield_sprites'][2]
