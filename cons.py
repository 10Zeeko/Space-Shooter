import pygame

debug = True
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
BULLET_SPRITE = pygame.image.load('assets/bullets/playerBullet.png')

'''
Enemy Constants
'''
# Enemy properties
ENEMY_VEL = 0.2 

# Enemy sprite
ENEMY_IDLE = pygame.image.load('assets/enemy/enemyShip.png')
