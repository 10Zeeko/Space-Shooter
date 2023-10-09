import pygame
import player
import bullet

FPS=60
WINDOW_SIZE_X=800
WINDOW_SIZE_Y=800

def main():
    pygame.init()
    screen = pygame.display.set_mode([WINDOW_SIZE_X, WINDOW_SIZE_Y])
    game_icon = pygame.image.load('assets/icon.png')
    background_image = pygame.image.load('assets/background.png')
    background_size = background_image.get_rect()
    player1 = player.create_player()

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
        player.player_update(player1, delta, screen, WINDOW_SIZE_X)

        pygame.display.flip()
    pygame.quit()

main()