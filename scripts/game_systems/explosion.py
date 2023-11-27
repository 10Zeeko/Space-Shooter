from ..game_config.cons import *

def create_effect(game_object, effects):
    effect = {
        'sprites': EXPLOSION_SPRITES,
        'current_sprite_index': 0,
        'x': game_object['x'] +20,
        'y': game_object['y'] +20,
        'start_time': pygame.time.get_ticks(),
    }
    effects.append(effect)

def explosion_update(effects):
    # Updates the sprite of the explosion to create a little animation
    for effect in effects:
        elapsed_time = pygame.time.get_ticks() - effect['start_time']
        if elapsed_time > 50:
            effect['current_sprite_index'] += 1
            if effect['current_sprite_index'] >= len(effect['sprites']):
                effects.remove(effect)  # Remove the effect after the last sprite
            else:
                effect['start_time'] = pygame.time.get_ticks()
