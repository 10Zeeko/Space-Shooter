from ..game_config.cons import *
from ..game_config.debug import debug_toggle
import math

def create_enemy(enemy_type, x, y):
    if enemy_type not in ENEMY_SPRITES:
        return None
    sprite = ENEMY_SPRITES[enemy_type]
    enemy = {
        'sprite': sprite,
        'enemy_type': enemy_type,
        'x': x - 40,
        'y': y - 350,
        'angle': 1.5,
        'last_rotation_time': time.time()
    }
    # Set hitbox size based on sprite size
    enemy['hitbox'] = sprite.get_rect(topleft=(enemy['x'], enemy['y']))
    return enemy

def draw_enemy(screen, enemy):
    sprite = enemy['sprite']
    square = sprite.get_rect().move(enemy['x'], enemy['y'])
    screen.blit(sprite, square)

    # Draw enemy hitbox for debugging
    if debug_toggle:
        pygame.draw.rect(screen, (0, 0, 255), enemy['hitbox'], 2)  # Blue rectangle

def move_enemy(enemy, delta, player):
    vel = int(ENEMY_VEL*delta)
    match enemy['enemy_type']:
        case 0:
            # ZigZag
            enemy['x'] += math.sin(pygame.time.get_ticks() * 0.002) * vel
            enemy['y'] = min(enemy['y'] + vel, 1000)
        case 1:
            # Straight
            enemy['y'] = min(enemy['y'] + vel * 1.25, 1000)
        case 2:
            # Move down until a certain distance
            if enemy['y'] < 100:
                enemy['y'] = min(enemy['y'] + vel, 100)
            else:
                # Circular movement
                enemy['x'] += math.sin(pygame.time.get_ticks() * 0.002) * vel
                enemy['y'] += math.cos(pygame.time.get_ticks() * 0.002) * vel
        case 3:
            # Rotate to a given direction (player direction) every second but it can only rotate 5º in that direction
            if time.time() - enemy['last_rotation_time'] >= 1 and enemy['y'] <= 600:
                dx = player['x'] - enemy['x']
                dy = player['y'] - enemy['y']
                target_angle = math.atan2(dy, dx)
                current_angle = enemy['angle']
                diff_angle = target_angle - current_angle
                if diff_angle > math.pi:
                    diff_angle -= 2*math.pi
                elif diff_angle < -math.pi:
                    diff_angle += 2*math.pi
                diff_angle = max(min(diff_angle, math.radians(20)), math.radians(-20))
                enemy['angle'] += diff_angle
                enemy['last_rotation_time'] = time.time()
            enemy['x'] += math.cos(enemy['angle']) * vel * 2
            enemy['y'] += math.sin(enemy['angle']) * vel * 2
    enemy['hitbox'].topleft = (enemy['x'], enemy['y'])

def enemy_update(enemy, delta, screen, player):
    move_enemy(enemy, delta, player)
    draw_enemy(screen, enemy)

def spawn_enemies(enemies, wave_enemies):
    if len(enemies) == 0 and len(wave_enemies) > 0:
        for j, enemy_row in enumerate(wave_enemies):
            num_enemies = len(enemy_row)
            x_spacing = WINDOW_SIZE_X // (num_enemies + 1)  # Calculate spacing between enemies
            y = j * 100  # Calculate y-coordinate for this row
            for i, enemy_type in enumerate(enemy_row):
                if enemy_type != 4:  # Don't spawn an enemy for number 4
                    x = (i + 1) * x_spacing  # Calculate x-coordinate for this enemy
                    new_enemy = create_enemy(enemy_type, x, y)
                    enemies.append(new_enemy)
        wave_enemies.clear()
    return enemies, wave_enemies

def update_enemies(enemies, delta, screen, _player):
    for enemy_object in enemies:
        if enemy_object['y'] > 900:
            enemies.remove(enemy_object)
        else:
            enemy_update(enemy_object, delta, screen, _player)