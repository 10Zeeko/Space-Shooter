from cons import *
import debug

def create_enemy(enemy_type, x, y):
    if enemy_type not in ENEMY_SPRITES:
        return None
    sprite = ENEMY_SPRITES[enemy_type]
    enemy = {
        'sprite': sprite,
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
    enemy['y'] = min(enemy['y'] + vel, 800)

    enemy['hitbox'].topleft = (enemy['x'], enemy['y'])

def enemy_update(enemy, delta, screen):
    move_enemy(enemy, delta)
    draw_enemy(screen, enemy)