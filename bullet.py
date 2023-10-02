import pygame

BULLET_VEL = 0.6

def create_bullet():
    bullet = {
        'sprite': pygame.image.load('assets/bullets/playerBullet.png'),
        'x':400-50,
        'y':800-76
    }
    return bullet

def draw_bullet(screen, bullet):
    sprite = bullet['sprite']
    square = sprite.get_rect().move(bullet['x'], bullet['y'])
    screen.blit(sprite, square)

def move_bullet(bullet, delta, size_y):
    vel = int(BULLET_VEL*delta)
    keys = pygame.key.get_pressed()
    bullet['y'] = max(bullet['y'] - vel, 0)