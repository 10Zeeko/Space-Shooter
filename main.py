# Game essential 
from scripts.game_config.cons import *
from scripts.game_systems.collisions_manager import *
from scripts.game_systems.effects_manager import *
from scripts.enemy.enemy_waves import *

# Game Objects
from scripts.player import player
from scripts.enemy import enemy
from scripts.hud import hud

from pygame.locals import *
import sys

def init_game():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
    game_icon = pygame.image.load('assets/icon.png')
    background_image = pygame.image.load('assets/background.png')
    background_size = background_image.get_rect()
    pygame.display.set_caption('Space Shooter')
    pygame.display.set_icon(game_icon)
    return screen, game_icon, background_image, background_size

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def main_menu(_screen, mainClock, background_image, going):
    MAIN_MENU_LOOP.play(-1)
    while going:
        _screen.blit(background_image, (0, 0))

        draw_text('Space Shooter', pygame.font.Font(None, 50), (255, 255, 255), _screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                MAIN_MENU_LOOP.stop()
                SPACE_LOOP.play(-1)
                return True
        if button_2.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                going = False
                pygame.quit()
                sys.exit()
        pygame.draw.rect(_screen, (100, 100, 100), button_1)
        pygame.draw.rect(_screen, (100, 100, 100), button_2)

        draw_text('Play', pygame.font.Font(None, 50), (255, 255, 255,), _screen, 50 + 50, 100 + 10)
        draw_text('Quit', pygame.font.Font(None, 50), (255, 255, 255), _screen, 50 + 50, 200 + 10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)

def game_over(_screen, mainClock, background_image, going):
    SPACE_LOOP.stop()
    GAME_OVER_LOOP.play(-1)
    while going:
        _screen.blit(background_image, (0, 0))

        draw_text('Game Over :(', pygame.font.Font(None, 50), (255, 255, 255), _screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                GAME_OVER_LOOP.stop()
                return True
        if button_2.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(_screen, (100, 100, 100), button_1)
        pygame.draw.rect(_screen, (100, 100, 100), button_2)

        draw_text('Play Again', pygame.font.Font(None, 50), (255, 255, 255), _screen, 50 + 10, 100 + 10)
        draw_text('Quit', pygame.font.Font(None, 50), (255, 255, 255), _screen, 50 + 50, 200 + 10)

        for event in pygame.event.get():
            if event.type == QUIT:
                GAME_OVER_LOOP.stop()
                going = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    GAME_OVER_LOOP.stop()
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)

def you_win(_screen, mainClock, background_image, player1, going):
    SPACE_LOOP.stop()
    WIN_LOOP.play(-1)
    while going:
        _screen.blit(background_image, (0, 0))

        draw_text('You Won!', pygame.font.Font(None, 50), (255, 255, 255), _screen, 20, 20)
        draw_text('Score: ' + str(player1['score']), pygame.font.Font(None, 50), (255, 255, 255), _screen, 20, 60)

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        if button_1.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                WIN_LOOP.stop()
                return True
        if button_2.collidepoint((mx, my)):
            if pygame.mouse.get_pressed()[0]:
                WIN_LOOP.stop()
                going = False
                pygame.quit()
                sys.exit()
        pygame.draw.rect(_screen, (100, 100, 100), button_1)
        pygame.draw.rect(_screen, (100, 100, 100), button_2)

        draw_text('Play Again', pygame.font.Font(None, 50), (255, 255, 255), _screen, 50 + 10, 100 + 10)
        draw_text('Quit', pygame.font.Font(None, 50), (255, 255, 255), _screen, 50 + 50, 200 + 10)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        mainClock.tick(60)

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