from ..enemy.enemy_behavior import *
from ..game_config.debug import *
from ..player.bullet import *
from ..player.power_ups import *
from ..game_systems.effects_manager import *
from ..game_systems.effects_manager import *

def create_enemy(enemy_type, x, y):
    if enemy_type not in ENEMY_SPRITES:
        return None
    sprite = ENEMY_SPRITES[enemy_type]
    enemy = {
        'sprites': sprite,
        'enemy_type': enemy_type,
        'x': x - 40,
        'y': y - 350,
        'angle': 1.5,
        'hp': 2,
        'value': 50,
        'last_rotation_time': time.time(),
        'bullets':[],
        'bullet_cooldown': 1
    }
    # Set hitbox size based on sprite size
    enemy['hitbox'] = sprite.get_rect(topleft=(enemy['x'], enemy['y']))
    match enemy_type:
        case 0:
            enemy['value'] = 100
        case 1:
            enemy['value'] = 50
        case 2:
            enemy['value'] = 150
        case 3:
            enemy['value'] = 100
    return enemy

def draw_enemy(screen, enemy):
    global debug_toggle
    sprite = enemy['sprites']
    square = sprite.get_rect().move(enemy['x'], enemy['y'])
    screen.blit(sprite, square)

    # Draw enemy hitbox for debugging
    if get_debug_toggle():
        pygame.draw.rect(screen, (0, 0, 255), enemy['hitbox'], 2)  # Blue rectangle

def create_enemy_bullet(enemy, angle, bullets):
    enemy_bullet_type = 1
    if enemy['enemy_type'] == 2:
        enemy_bullet_type = 2
    enemy_bullet = create_bullet(enemy['x'] + 45.5, enemy['y'] + 70, enemy_bullet_type)
    enemy_bullet['angle'] = angle
    bullets.append(enemy_bullet)

def enemy_update(enemy, delta, screen, player, bullets):
    move_enemy(enemy, delta, player)
    update_effects_game_object(enemy)
    draw_enemy(screen, enemy)

    # Make the enemy shoot bullets
    if time.time() - enemy['bullet_cooldown'] >= 1 and enemy['y'] > 30:
        ENEMY_SOUND.play()
        match enemy['enemy_type']:
            case 2:
                create_enemy_bullet(enemy, 45, bullets)
                create_enemy_bullet(enemy, 90, bullets)
            case 3:
                pass
            case other:
                create_enemy_bullet(enemy, math.pi / 2, bullets)
        enemy['bullet_cooldown'] = time.time()


def spawn_enemies(enemies, wave_enemies):
    if len(enemies) == 0 and len(wave_enemies) > 0:
        for j, enemy_row in enumerate(wave_enemies):
            num_enemies = len(enemy_row)
            x_spacing = WINDOW_SIZE_X // (num_enemies + 1)  # Calculate spacing between enemies
            y = j * 100  # Calculate y-coordinate for this row
            for i, enemy_type in enumerate(enemy_row):
                if enemy_type != 4:  # Don't spawn an enemy for number 4
                    x = (i + 1) * x_spacing  # Calculate x-coordinate for this enemy
                    new_enemy = create_enemy(enemy_type, x, y)
                    enemies.append(new_enemy)
        wave_enemies.clear()
    return enemies, wave_enemies

def update_enemies(enemies, delta, screen, _player, bullets):
    for enemy_object in enemies:
        if enemy_object['y'] > 900:
            enemies.remove(enemy_object)
        else:
            enemy_update(enemy_object, delta, screen, _player, bullets)

def enemy_hit(enemy, enemies, power_ups, effects):
    enemy['hp'] -= 1
    blink(enemy, (255, 0, 0), 1, 150)
    if enemy['hp'] == 0:
        create_effect(enemy, effects)
        # 30% chance to drop a power-up
        if random.random() < 0.3:
            # Choose a random power-up type
            power_up_type = random.choice([0, 1, 2, 3])
            print (power_up_type)
            new_power_up = create_power_up(power_up_type, enemy['x'], enemy['y'])
            power_ups.append(new_power_up)
        enemies.remove(enemy)
        return enemy['value']
    return 0