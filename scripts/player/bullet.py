from ..game_config.cons import *
from ..game_config.debug import debug_toggle

def create_bullet(x, y, bullet_type):
    bullet = {
        'sprite': BULLET_SPRITE[bullet_type],
        'x': x + 50 - 4.5, # 50 is player width
        'y': y - 18.5,
        'bullet_type': bullet_type
    }

    # If it's an enemy bullet, flip the sprite vertically
    if bullet_type:
        bullet['sprite'] = pygame.transform.flip(bullet['sprite'], False, True)

    bullet['hitbox'] = pygame.Rect(bullet['x'], bullet['y'], 9, 37)
    return bullet

def draw_bullet(screen, bullet):
    global debug_toggle
    sprite = bullet['sprite']
    square = sprite.get_rect().move(bullet['x'], bullet['y'])
    screen.blit(sprite, square)

    # Draw bullet hitbox for debugging
    if debug_toggle:
        pygame.draw.rect(screen, (255, 255, 0), bullet['hitbox'], 2)  # Yellow rectangle

def move_bullet(bullet, delta, shooting_enemy):
    vel = int(BULLET_VEL*delta)
    if shooting_enemy:
        vel *= -1
    bullet['y'] = max(bullet['y'] - vel, -30)

    # Update the hitbox position to move with the bullet
    bullet['hitbox'].topleft = (bullet['x'], bullet['y'])

def update_bullets(bullet, delta, screen, enemies, shooting_enemy):
    move_bullet(bullet, delta, shooting_enemy)
    draw_bullet(screen, bullet)