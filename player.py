import pygame
import bullet

PLAYER_VEL = 0.4
BULLET_COOLDOWN = 400

def create_player():
    player = {
        'right': pygame.image.load('assets/ship/playerShipRight.png'),
        'left': pygame.image.load('assets/ship/playerShipLeft.png'),
        'idle': pygame.image.load('assets/ship/playerShip.png'),
        'lives': 3,
        'score': 0,
        'bullets':[],
        'bullet_cooldown': 0,
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
    if keys[pygame.K_SPACE]:
        now = pygame.time.get_ticks()
        if now - player['bullet_cooldown'] >= BULLET_COOLDOWN:
            player['bullet_cooldown'] = pygame.time.get_ticks()
            player_bullet = bullet.create_bullet(player['x'], player['y'])
            player['bullets'].append(player_bullet)
    if not moved:
        player['sprites'] = player['idle']

def player_update(player, delta, screen, size_x, enemies):
    move_player(player, delta, size_x)
    draw_player(screen, player)
    player['bullets'] = [bullet_object for bullet_object in player['bullets'] if bullet_object['y'] > -30]
    for bullet_object in player['bullets']:
        bullet.move_bullet(bullet_object, delta)
        bullet.draw_bullet(screen, bullet_object)

        # Check for collisions with enemies
        for enemy in enemies:
            if pygame.Rect(bullet_object['x'], bullet_object['y'], 9, 37).colliderect(pygame.Rect(enemy['x'], enemy['y'], 100, 100)):
                player['score'] += 100
                enemies.remove(enemy)
                player['bullets'].remove(bullet_object)
                break