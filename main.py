# Game essential 
from scripts.game_config.cons import *
from scripts.game_systems.collisions_manager import *
from scripts.game_systems.effects_manager import *
from scripts.enemy.enemy_waves import *
from pygame.locals import *
from scripts.game_systems.scene_manager import *
# Game Objects
from scripts.player import player
from scripts.enemy import enemy
from scripts.hud import hud

def init_game():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
    game_icon = pygame.image.load('assets/icon.png')
    background_image = pygame.image.load('assets/background.png')
    background_size = background_image.get_rect()
    pygame.display.set_caption('Space Shooter')
    pygame.display.set_icon(game_icon)
    return screen, game_icon, background_image, background_size

def handle_events(player1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.USEREVENT + 1:
            player1['invincible'] = False
            POWER_UP_DROP_SOUND.play()
            pygame.time.set_timer(pygame.USEREVENT + 1, 0)
        elif event.type == pygame.USEREVENT + 2:
            player1['speed_boost'] = False
            POWER_UP_DROP_SOUND.play()
            pygame.time.set_timer(pygame.USEREVENT + 2, 0)
        elif event.type == pygame.USEREVENT + 3:
            player1['double_laser'] = False
            POWER_UP_DROP_SOUND.play()
            pygame.time.set_timer(pygame.USEREVENT + 3, 0)
    return True

def main():
    screen, game_icon, background_image, background_size = init_game()
    clock = pygame.time.Clock()
    going = True
    while (going):
        player1 = player.create_player()
        power_ups = []
        bullets = []
        effects = []
        wave_round = 0
        enemies, wave_enemies = create_wave(wave_round)
        if not main_menu(screen, clock, background_image, going):
            return
        while player1['alive'] and going:
            delta = clock.tick(FPS)
            going = handle_events(player1)
            screen.blit(background_image,background_size)
            player_update(player1, delta, screen, bullets)
            enemies, wave_enemies = enemy.spawn_enemies(enemies, wave_enemies)
            if len(enemies) == 0 and len(wave_enemies) == 0:
                wave_round += 1
                if wave_round < 5:  # Check if there are more waves
                    wave_enemies = return_enemy_wave(wave_round)
                else:  # No more waves, player wins
                    if not you_win(screen, clock, background_image, player1, going):
                        return
                    else:  # Reset game state for new game
                        break
            enemy.update_enemies(enemies, delta, screen, player1, bullets)
            # Update power-ups
            for power_up in power_ups:
                update_power_up(power_up, delta, screen)
            # Update bullets
            for bullet_object in bullets:
                update_bullets(bullet_object, delta, screen)
            check_all_collisions(player1, enemies, power_ups, bullets, effects)
            draw_effects(screen, effects)
            explosion_update(effects)
            hud.draw_hud(screen, player1)
            pygame.display.flip()
        if not game_over(screen, clock, background_image, going):
            return
    pygame.quit()

main()