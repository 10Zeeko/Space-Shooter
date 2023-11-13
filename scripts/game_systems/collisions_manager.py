from ..player.player import *
from ..player.bullet import *
from ..enemy.enemy import *

def check_collision(object1, object2):
    # Check if the hitboxes of the two objects are colliding
    return object1['hitbox'].colliderect(object2['hitbox'])

def check_all_collisions(player, enemies, power_ups):
    # Check for collisions between player and enemies
    for enemy in enemies:
        if check_collision(player, enemy):
            # Handle player-enemy collision
            handle_damage_player(player)
            enemies.remove(enemy)

    # Check for collisions between player's bullets and enemies
    for bullet in player['bullets']:
        for enemy in enemies:
            if check_collision(enemy, bullet):
                # Handle enemy-bullet collision
                value = enemy_hit(enemy, enemies, player['bullets'], bullet, power_ups)
                add_points_to_score(player, value)

    # Check for collisions between enemy's bullets and player
    for enemy in enemies:
        for bullet in enemy['bullets']:
            if check_collision(player, bullet):
                # Handle player-bullet collision
                handle_damage_player(player)
                enemy['bullets'].remove(bullet)
    
     # Check for collisions between player and power-ups
    for power_up in power_ups:
        if check_collision(player, power_up):
            # Handle player-power-up collision
            activate_power_up(player, power_up)
            power_ups.remove(power_up)

def handle_damage_player(player):
    if player['shield']:
        player['shield'] = False
        print ("No more shield")
    elif player['invincible']:
        pass
    else:
        player_hit(player)