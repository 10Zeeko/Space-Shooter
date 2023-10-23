# Game essential 
from cons import *
from enemy_waves import return_enemy_wave

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
    wave_round = 0
    wave_enemies = return_enemy_wave(wave_round)

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
        if len(enemies) == 0 and len(wave_enemies) > 0:
            for j, enemy_row in enumerate(wave_enemies):
                num_enemies = len(enemy_row)
                x_spacing = WINDOW_SIZE_X // (num_enemies + 1)  # Calculate spacing between enemies
                y = j * 100  # Calculate y-coordinate for this row
                for i, enemy_type in enumerate(enemy_row):
                    if enemy_type != 4:  # Don't spawn an enemy for number 4
                        x = (i + 1) * x_spacing  # Calculate x-coordinate for this enemy
                        new_enemy = enemy.create_enemy(enemy_type, x, y)
                        enemies.append(new_enemy)
            wave_enemies.clear()

        # If all enemies are defeated, move on to the next wave
        if len(enemies) == 0 and len(wave_enemies) == 0:
            wave_round += 1
            if wave_round < 4:  # Check if there are more waves
                wave_enemies = return_enemy_wave(wave_round)
        
        # Update and draw enemies
        for enemy_object in enemies:
            enemy.enemy_update(enemy_object, delta, screen)
        
        hud.draw_hud(screen, player1)
        
        pygame.display.flip()
    pygame.quit()

main()