from cons import *
import debug
import math

def create_enemy(enemy_type, x, y):
    if enemy_type not in ENEMY_SPRITES:
        return None
    sprite = ENEMY_SPRITES[enemy_type]
    enemy = {
        'sprite': sprite,
        'enemy_type': enemy_type,
        'x': x - 40,
        'y': y - 350
    }
    # Set hitbox size based on sprite size
    enemy['hitbox'] = sprite.get_rect(topleft=(enemy['x'], enemy['y']))
    return enemy

def draw_enemy(screen, enemy):
    sprite = enemy['sprite']
    square = sprite.get_rect().move(enemy['x'], enemy['y'])
    screen.blit(sprite, square)

    global debug_toggle
    # Draw enemy hitbox for debugging
    if debug.debug_toggle:
        pygame.draw.rect(screen, (0, 0, 255), enemy['hitbox'], 2)  # Blue rectangle

def move_enemy(enemy, delta):
    vel = int(ENEMY_VEL*delta)
    match enemy['enemy_type']:
        case 0:
            # ZigZag
            enemy['x'] += math.sin(pygame.time.get_ticks() * 0.002) * vel
            enemy['y'] = min(enemy['y'] + vel, 800)
        case 1:
            # Straight
            enemy['y'] = min(enemy['y'] + vel, 800)
        case 2:
            # Move down until a certain distance
            if enemy['y'] < 100:
                enemy['y'] = min(enemy['y'] + vel, 100)
            else:
                # Circular movement
                enemy['x'] += math.sin(pygame.time.get_ticks() * 0.002) * vel
                enemy['y'] += math.cos(pygame.time.get_ticks() * 0.002) * vel
        case 3:
            # Rotate to a given direction every second
            if pygame.time.get_ticks() % 1000 < delta * 1000:  # Check if a second has passed
                angle = math.radians(5)  # Convert degrees to radians
                x = enemy['x']
                y = enemy['y']
                # Rotate the point around the origin (0, 0)
                enemy['x'] = x * math.cos(angle) - y * math.sin(angle)
                enemy['y'] = y * math.cos(angle) + x * math.sin(angle)
    enemy['hitbox'].topleft = (enemy['x'], enemy['y'])
    enemy['hitbox'].topleft = (enemy['x'], enemy['y'])

def enemy_update(enemy, delta, screen):
    move_enemy(enemy, delta)
    draw_enemy(screen, enemy)