import pygame
import time
import random

'''
Game Window Constants
'''
FPS = 60
WINDOW_SIZE_X = 800
WINDOW_SIZE_Y = 800

'''
HUD Constants
'''
SCORE_TEXT_SIZE = 12
LIVES_TEXT_SIZE = 12

'''
Player Constants
'''
# Player properties
PLAYER_VEL = 0.4
BULLET_COOLDOWN = 400

# Player sprites
PLAYER_RIGHT = pygame.image.load('assets/ship/playerShipRight.png')
PLAYER_LEFT = pygame.image.load('assets/ship/playerShipLeft.png')
PLAYER_IDLE = pygame.image.load('assets/ship/playerShip.png')

'''
Bullet Constants
'''
# Bullet properties
BULLET_VEL = 0.6

# Bullet sprite
BULLET_SPRITE = {
    0: pygame.image.load('assets/bullets/playerBullet.png'),
    1: pygame.image.load('assets/bullets/enemyBullet.png'),
    2: pygame.image.load('assets/bullets/laserRed.png')
}

'''
Power Ups Constants
'''
POWER_UP_SPEED = 0.2

POWER_UP_SPRITES = {
    0: pygame.image.load('assets/power_ups/invencivility.png'),
    1: pygame.image.load('assets/power_ups/speed.png'),
    2: pygame.image.load('assets/power_ups/shield.png'),
    3: pygame.image.load('assets/power_ups/double.png')
}

SHIELD_SPRITE = {
    0: pygame.image.load('assets/power_ups/shield1.png'),
    1: pygame.image.load('assets/power_ups/shield2.png'),
    2: pygame.image.load('assets/power_ups/shield3.png')
}

'''
Enemy Constants
'''
# Enemy properties
ENEMY_VEL = 0.1

# Enemy sprite
ENEMY_SPRITES = {
    0: pygame.image.load('assets/enemy/enemyCommon.png'),
    1: pygame.image.load('assets/enemy/enemyDoubleLaser.png'),
    2: pygame.image.load('assets/enemy/enemyCrossedLaser.png'),
    3: pygame.image.load('assets/enemy/enemyFast.png')
}