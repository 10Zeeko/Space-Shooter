from ..game_config.cons import *
import math

def move_enemy(enemy, delta, player):
    vel = int(ENEMY_VEL*delta)
    match enemy['enemy_type']:
        case 0:
            # ZigZag
            enemy['x'] += math.sin(pygame.time.get_ticks() * 0.002) * vel
            enemy['y'] = min(enemy['y'] + vel, 1000)
        case 1:
            # Straight
            enemy['y'] = min(enemy['y'] + vel * 1.25, 1000)
        case 2:
            # Move down until a certain distance
            if enemy['y'] < 100:
                enemy['y'] = min(enemy['y'] + vel, 100)
            else:
                # Circular movement
                enemy['x'] += math.sin(pygame.time.get_ticks() * 0.002) * vel
                enemy['y'] += math.cos(pygame.time.get_ticks() * 0.002) * vel
        case 3:
            # Rotate to a given direction (player direction) every second but it can only rotate 5º in that direction
            if time.time() - enemy['last_rotation_time'] >= 1 and enemy['y'] <= 600:
                dx = player['x'] - enemy['x']
                dy = player['y'] - enemy['y']
                target_angle = math.atan2(dy, dx)
                current_angle = enemy['angle']
                diff_angle = target_angle - current_angle
                if diff_angle > math.pi:
                    diff_angle -= 2*math.pi
                elif diff_angle < -math.pi:
                    diff_angle += 2*math.pi
                diff_angle = max(min(diff_angle, math.radians(20)), math.radians(-20))
                enemy['angle'] += diff_angle
                enemy['last_rotation_time'] = time.time()
            enemy['x'] += math.cos(enemy['angle']) * vel * 2
            enemy['y'] += math.sin(enemy['angle']) * vel * 2
    enemy['hitbox'].topleft = (enemy['x'], enemy['y'])