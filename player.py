import pygame

PLAYER_VEL = 0.4

def create_player():
    player = {
        'right': pygame.image.load('assets/ship/playerShipRight.png'),
        'left': pygame.image.load('assets/ship/playerShipLeft.png'),
        'idle': pygame.image.load('assets/ship/playerShip.png'),
        'x':400-50,
        'y':800-76
    }
    player['sprites'] = player['idle']
    return player

def draw_player(screen, player):
    sprite = player['sprites']
    square = sprite.get_rect().move(player['x'], player['y'])
    screen.blit(sprite, square)

def move_player(player, delta, size_x):
    moved = False
    vel = int(PLAYER_VEL*delta)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player['x']>0:
        player['x'] = max(player['x'] - vel, 0)
        player['sprites'] = player['left']
        moved = True
    if keys[pygame.K_RIGHT] and player['x']<size_x-100:
        player['x']=min(player['x']+vel, size_x-50)
        player['sprites']=player['right']
        moved=True
    if not moved:
        player['sprites'] = player['idle']