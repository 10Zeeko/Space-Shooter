from cons import *
import debug

def create_enemy():
    enemy = {
        'sprite': ENEMY_IDLE,
        'x': 400-50,
        'y': 0
    }
    enemy['hitbox'] = pygame.Rect(enemy['x'], enemy['y'], 93, 84)
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