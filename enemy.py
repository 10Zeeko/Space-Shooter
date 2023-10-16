import pygame

ENEMY_VEL = 0.2

def create_enemy():
    enemy = {
        'sprite': pygame.image.load('assets/enemy/enemyShip.png'),
        'x': 400-50,
        'y': 0
    }
    return enemy

def draw_enemy(screen, enemy):
    sprite = enemy['sprite']
    square = sprite.get_rect().move(enemy['x'], enemy['y'])
    screen.blit(sprite, square)

def move_enemy(enemy, delta):
    vel = int(ENEMY_VEL*delta)
    enemy['y'] = min(enemy['y'] + vel, 800)

def enemy_update(enemy, delta, screen):
    move_enemy(enemy, delta)
    draw_enemy(screen, enemy)