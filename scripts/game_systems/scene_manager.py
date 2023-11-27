from ..game_config.cons import *
from ..game_systems.input_manager import *
import sys
from pygame.locals import *

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