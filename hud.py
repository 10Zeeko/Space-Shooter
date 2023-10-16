import pygame

SCORE_TEXT_SIZE = 12
LIVES_TEXT_SIZE = 12

def draw_text(screen, text, size, x, y):
    font = pygame.font.Font('assets/font/Kenney Space.ttf', size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_hud(screen, player):
    draw_text(screen, 'Score: ' + str(player['score']), SCORE_TEXT_SIZE, 10, 10)
    draw_text(screen, 'Lives: ' + str(player['lives']), LIVES_TEXT_SIZE, 700, 10)