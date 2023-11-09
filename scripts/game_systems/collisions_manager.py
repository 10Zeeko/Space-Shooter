from ..player.player import *
from ..player.bullet import *
from ..enemy.enemy import *

def check_collision(object1, object2):
    # Check if the hitboxes of the two objects are colliding
    return object1['hitbox'].colliderect(object2['hitbox'])

def check_all_collisions(player, enemies):
    # Check for collisions between player and enemies
    for enemy in enemies:
        if check_collision(player, enemy):
            # Handle player-enemy collision
            player_hit(player)
            enemies.remove(enemy)

    # Check for collisions between player's bullets and enemies
    for bullet in player['bullets']:
        for enemy in enemies:
            if check_collision(enemy, bullet):
                # Handle enemy-bullet collision
                enemy_hit(enemy, enemies, player['bullets'], bullet)

    # Check for collisions between enemy's bullets and player
    for enemy in enemies:
        for bullet in enemy['bullets']:
            if check_collision(player, bullet):
                # Handle player-bullet collision
                player_hit(player)
                enemy['bullets'].remove(bullet)