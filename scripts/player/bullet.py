from ..game_config.cons import *
from ..game_config.debug import debug_toggle

def create_bullet(x, y):
    bullet = {
        'sprite': BULLET_SPRITE,
        'x': x + 50 - 4.5, # 50 is player width
        'y': y - 18.5
    }
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

def move_bullet(bullet, delta):
    vel = int(BULLET_VEL*delta)
    bullet['y'] = max(bullet['y'] - vel, -30)

    # Update the hitbox position to move with the bullet
    bullet['hitbox'].topleft = (bullet['x'], bullet['y'])

def update_bullets(bullet, delta, screen, enemies):
    move_bullet(bullet, delta)
    draw_bullet(screen, bullet)
    # Check for collisions with enemies
    for enemy in enemies:
        if bullet['hitbox'].colliderect(pygame.Rect(enemy['x'], enemy['y'], 100, 100)):
            enemies.remove(enemy)
            return True
    return False