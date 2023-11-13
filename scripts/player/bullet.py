from ..game_config.cons import *
from ..game_config.debug import *
import math

def create_bullet(x, y, bullet_type):
    bullet = {
        'sprite': BULLET_SPRITE[bullet_type],
        'x': x,
        'y': y,
        'bullet_type': bullet_type,
        'shooting_enemy': True
    }
    width, height = bullet['sprite'].get_size()
    # If it's an enemy bullet, flip the sprite vertically
    if bullet_type == 1:
        bullet['sprite'] = pygame.transform.flip(bullet['sprite'], False, True)
    elif bullet_type == 2:
        smaller_sprite = pygame.transform.scale(bullet['sprite'], (width // 2, height // 2))
        bullet['sprite'] = smaller_sprite
        width = width / 2
        height = height / 2
    else:
        bullet['shooting_enemy'] = False
    bullet['hitbox'] = pygame.Rect(bullet['x'], bullet['y'], width, height)

    return bullet

def draw_bullet(screen, bullet):
    global debug_toggle
    sprite = pygame.transform.rotate(bullet['sprite'], bullet['angle'])
    square = sprite.get_rect().move(bullet['x'], bullet['y'])
    screen.blit(sprite, square)

    # Draw bullet hitbox for debugging
    if get_debug_toggle():
        pygame.draw.rect(screen, (255, 255, 0), bullet['hitbox'], 2)  # Yellow rectangle

def move_bullet(bullet, delta):
    vel = int(BULLET_VEL*delta)
    if bullet['shooting_enemy']:
        # Use the angle to calculate the new x and y positions
        bullet['x'] += math.cos(bullet['angle']) * vel
        bullet['y'] += math.sin(bullet['angle']) * vel
    else:
        bullet['y'] = max(bullet['y'] - vel, -100)
    bullet['hitbox'].topleft = (bullet['x'], bullet['y'])

def update_bullets(bullet, delta, screen):
    move_bullet(bullet, delta)
    draw_bullet(screen, bullet)