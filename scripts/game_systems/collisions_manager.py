from ..player.player import *
from ..player.bullet import *
from ..enemy.enemy import *
from ..game_systems.effects_manager import *

def check_collision(object1, object2):
    # Check if the hitboxes of the two objects are colliding
    return object1['hitbox'].colliderect(object2['hitbox'])
def check_pick_collision(object1, object2):
    # Check if the hitboxes of the two objects are colliding
    return object1['pick_hitbox'].colliderect(object2['hitbox'])

def check_all_collisions(player, enemies, power_ups, bullets):
    # Check for collisions between player and enemies
    for enemy in enemies:
        if check_collision(player, enemy):
            # Handle player-enemy collision
            handle_damage_player(player)
            enemies.remove(enemy)

    # Check for collisions between player's bullets and enemies
    for bullet in bullets:
        for enemy in enemies:
            if check_collision(enemy, bullet) and not bullet['shooting_enemy']:
                # Handle enemy-bullet collision
                value = enemy_hit(enemy, enemies, power_ups)
                add_points_to_score(player, value)
                remove_bullet(bullets, bullet)
        if check_collision(player, bullet) and bullet['shooting_enemy']:
            # Handle player-bullet collision
            handle_damage_player(player)
            remove_bullet(bullets, bullet)
        elif bullet['y'] <= -100 or bullet['y'] >= 900:
            remove_bullet(bullets, bullet)
    
     # Check for collisions between player and power-ups
    for power_up in power_ups:
        if check_pick_collision(player, power_up):
            # Handle player-power-up collision
            activate_power_up(player, power_up)
            power_ups.remove(power_up)

def remove_bullet(bullets, bullet):
    try:
        bullets.remove(bullet)
    except ValueError:
        pass  # Do nothing if bullet is not in the list

def handle_damage_player(player):
    if player['shield']:
        player['shield'] = False
        print ("No more shield")
    elif player['invincible']:
        pass
    else:
        player_hit(player)