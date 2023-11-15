from ..game_config.cons import *
from ..game_config.debug import *

def create_power_up(power_up_type, x, y):
    power_up = {
        'sprite': POWER_UP_SPRITES[power_up_type],
        'power_up_type': power_up_type,
        'x': x,
        'y': y,
    }
    width, height = power_up['sprite'].get_size()
    power_up['hitbox'] = pygame.Rect(power_up['x'], power_up['y'], width, height)
    return power_up

def draw_power_up(screen, power_up):
    sprite = power_up['sprite']
    square = sprite.get_rect().move(power_up['x'], power_up['y'])
    screen.blit(sprite, square)

    if get_debug_toggle():
        pygame.draw.rect(screen, (0, 255, 0), power_up['hitbox'], 2)

def move_power_up(power_up, delta):
    vel = int(POWER_UP_SPEED*delta)
    power_up['y'] += vel
    power_up['hitbox'].topleft = (power_up['x'], power_up['y'])

def update_power_up(power_up, delta, screen):
    move_power_up(power_up, delta)
    draw_power_up(screen, power_up)