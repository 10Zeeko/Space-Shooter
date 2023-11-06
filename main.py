# Game essential 
from cons import *
from enemy_waves import *

# Game Objects
import player
import enemy
import hud

def init_game():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
    game_icon = pygame.image.load('assets/icon.png')
    background_image = pygame.image.load('assets/background.png')
    background_size = background_image.get_rect()
    pygame.display.set_caption('Space Shooter')
    pygame.display.set_icon(game_icon)
    return screen, game_icon, background_image, background_size

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main():
    screen, game_icon, background_image, background_size = init_game()
    player1 = player.create_player()
    wave_round = 0
    enemies, wave_enemies = create_wave(wave_round)
    clock = pygame.time.Clock()
    going = True
    while (going):
        delta = clock.tick(FPS)
        going = handle_events()
        screen.blit(background_image,background_size)
        player.player_update(player1, delta, screen, enemies)
        enemies, wave_enemies = enemy.spawn_enemies(enemies, wave_enemies)
        if len(enemies) == 0 and len(wave_enemies) == 0:
            wave_round += 1
            if wave_round < 4:  # Check if there are more waves
                wave_enemies = return_enemy_wave(wave_round)
        enemy.update_enemies(enemies, delta, screen, player1)
        hud.draw_hud(screen, player1)
        pygame.display.flip()
    pygame.quit()

main()