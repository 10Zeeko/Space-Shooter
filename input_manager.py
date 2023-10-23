import pygame

RIGHT_KEY = [pygame.K_RIGHT, pygame.K_d]
LEFT_KEY = [pygame.K_LEFT, pygame.K_a]
SHOOT_KEYS = [pygame.K_SPACE, pygame.K_w, pygame.K_UP]
DEBUG_KEY = pygame.K_p

# This variable is only for debug
debug_key_released = True

def right_input(keys):
    return any(keys[key] for key in RIGHT_KEY)

def left_input(keys):
    return any(keys[key] for key in LEFT_KEY)

def shoot_input(keys):
    return any(keys[key] for key in SHOOT_KEYS)

def debug_input(keys):
    global debug_key_released
    if keys[DEBUG_KEY]:
        if debug_key_released:
            debug_key_released = False
            return True
    else:
        debug_key_released = True
    return False