import pygame

BULLET_VEL = 0.6

def create_bullet(x, y):
    bullet = {
        'sprite': pygame.image.load('assets/bullets/playerBullet.png'),
        'x': x + 50 - 4.5, # 50 is player width
        'y': y - 18.5
    }
    return bullet

def draw_bullet(screen, bullet):
    sprite = bullet['sprite']
    square = sprite.get_rect().move(bullet['x'], bullet['y'])
    screen.blit(sprite, square)

def move_bullet(bullet, delta):
    vel = int(BULLET_VEL*delta)
    bullet['y'] = max(bullet['y'] - vel, -30)