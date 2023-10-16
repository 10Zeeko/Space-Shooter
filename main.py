# Game essential 
from cons import *

# Game Objects
import player
import enemy
import hud

def main():
    # Game
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
    game_icon = pygame.image.load('assets/icon.png')
    background_image = pygame.image.load('assets/background.png')
    background_size = background_image.get_rect()

    # Player
    player1 = player.create_player()

    # Enemies
    enemies = []
    enemy_spawn_timer = 0
    ENEMY_SPAWN_RATE = 2000

    pygame.display.set_caption('Space Shooter')
    pygame.display.set_icon(game_icon)

    clock = pygame.time.Clock()
    going = True
    while (going):
        delta = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
        screen.blit(background_image,background_size)
        player.player_update(player1, delta, screen, enemies)

        # Spawn enemies
        now = pygame.time.get_ticks()
        if now - enemy_spawn_timer >= ENEMY_SPAWN_RATE:
            enemy_spawn_timer = now
            new_enemy = enemy.create_enemy()
            enemies.append(new_enemy)
        
        # Update and draw enemies
        for enemy_object in enemies:
            enemy.enemy_update(enemy_object, delta, screen)
        
        hud.draw_hud(screen, player1)
        
        pygame.display.flip()
    pygame.quit()

main()