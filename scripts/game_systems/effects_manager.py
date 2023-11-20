import pygame

def blink(game_object, blink_color, blink_times, blink_duration):
    # Save the original image
    original_image = game_object['sprites']

    # Create a copy of the original image
    blink_image = original_image.copy()

    # Create a surface filled with the blink color
    overlay = pygame.Surface(original_image.get_size(), pygame.SRCALPHA)
    overlay.fill(blink_color)

    # Blend the overlay with the non-transparent pixels of the blink image
    for x in range(overlay.get_width()):
        for y in range(overlay.get_height()):
            if blink_image.get_at((x, y))[3] > 0:  # If the pixel is not transparent
                original_color = blink_image.get_at((x, y))
                overlay_color = overlay.get_at((x, y))
                blended_color = [0, 0, 0, original_color[3]]  # Keep the original alpha
                for i in range(3): 
                    blended_color[i] = min(original_color[i] + overlay_color[i], 255)
                blink_image.set_at((x, y), blended_color)

    # Set the start time of the blinking effect
    game_object['blink_start_time'] = pygame.time.get_ticks()

    # Set the blink parameters
    game_object['blink_image'] = blink_image
    game_object['original_image'] = original_image
    game_object['blink_times'] = blink_times
    game_object['blink_duration'] = blink_duration
    game_object['blink_phase'] = 0

def update_game_object(game_object):
    # Update the blinking effect
    if 'blink_start_time' in game_object:
        elapsed_time = pygame.time.get_ticks() - game_object['blink_start_time']
        total_blink_time = game_object['blink_times'] * game_object['blink_duration']

        if elapsed_time < total_blink_time:
            blink_phase_duration = game_object['blink_duration'] / 2
            game_object['blink_phase'] = int(elapsed_time / blink_phase_duration) % 2

            if game_object['blink_phase'] == 0:
                print ("Blink")
                game_object['sprites'] = game_object['blink_image']
            else:
                print ("Original")
                game_object['sprites'] = game_object['original_image']
        else:
            # End the blinking effect
            print ("Finish")
            game_object['sprites'] = game_object['original_image']
            del game_object['blink_start_time']