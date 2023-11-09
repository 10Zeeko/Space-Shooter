from ..game_config.cons import *
from . import bullet
from ..game_config.debug import *
from ..game_systems.input_manager import *



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
        'y':800-76
    }
    player['sprites'] = player['idle']
    player['hitbox'] = pygame.Rect(player['x'] + 35, player['y'] + 5, 29, 95)
    return player

def draw_player(screen, player):
    sprite = player['sprites']
    square = sprite.get_rect().move(player['x'], player['y'])
    screen.blit(sprite, square)

    # Draw player hitbox for debugging
    if get_debug_toggle():
        pygame.draw.rect(screen, (255, 0, 0), player['hitbox'], 2)  # Red rectangle

def move_player(player, delta):
    global debug_toggle
    moved = False
    vel = int(PLAYER_VEL*delta)
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
            player_bullet = bullet.create_bullet(player['x'], player['y'], 0)
            player['bullets'].append(player_bullet)
    if debug_input(keys):
        debug_value = not get_debug_toggle()
        set_debug_toggle(debug_value)
    if not moved:
        player['sprites'] = player['idle']

    # Update the hitbox position to move with the player
    player['hitbox'].topleft = (player['x'] + 35, player['y'] + 5)

def player_update(player, delta, screen, enemies):
    move_player(player, delta)
    draw_player(screen, player)
    check_colliosins(player, enemies)
    # Update bullet position and check collisions
    player['bullets'] = [bullet_object for bullet_object in player['bullets'] if bullet_object['y'] > -30]
    for bullet_object in player['bullets']:
        check_coll = bullet.update_bullets(bullet_object, delta, screen, enemies, False)
        if check_coll:
            player['score'] += 100
            player['bullets'].remove(bullet_object)

    return True # Player is still alive

def check_colliosins(player, enemies):
    # Check player collisions with enemies
    player_rect = player['hitbox']  # PlayerHitBox 29 x 95
    for enemy in enemies:
        enemy_rect = pygame.Rect(enemy['x'], enemy['y'], 93, 84)  # assuming the enemy's size is 100x100
        if player_rect.colliderect(enemy_rect):
            player['lives'] -= 1
            enemies.remove(enemy)
            if player['lives'] == 0:
                break  # Player has no lives left

def player_hit(player):
    player['lives'] -= 1
    if player['lives'] == 0:
        print("Game Over")  # Player has no lives left