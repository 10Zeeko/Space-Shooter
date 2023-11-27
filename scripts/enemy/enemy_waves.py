def return_enemy_wave(wave_round):
    enemy_wave = [
        [
            [4, 4, 4, 4, 4, 4],
            [1, 4, 1, 1, 4, 1],
            [4, 4, 4, 4, 4, 4]
        ],
        [
            [4, 0, 4, 4, 0, 4],
            [4, 4, 0, 0, 4, 4],
            [4, 4, 4, 4, 4, 4]
        ],
        [
            [3, 4, 1, 1, 4, 3],
            [4, 4, 4, 4, 4, 4],
            [4, 4, 0, 0, 4, 4]
        ],
        [
            [4, 4, 1, 1, 4, 4],
            [3, 4, 4, 4, 4, 3],
            [4, 4, 4, 4, 4, 4]
        ]
    ]
    return enemy_wave[wave_round]

def create_wave(wave_round):
    enemies = []
    wave_enemies = return_enemy_wave(wave_round)
    return enemies, wave_enemies