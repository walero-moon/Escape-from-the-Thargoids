# This file will end up being huge, but that is to facilitate modifying
# player speed, projectile speed, projectile size, etc.

# Main game's window
BACKGROUND = "lib/game/sprites/background"
WIDTH = 1600
HEIGHT = 900

# Player's constants
P_SPRITES = "lib/game/sprites/player/ship_sprites"
P_LASER_SPRITES = "lib/game/sprites/player/laser_sprites" # Relative to repo root
P_SHOOT_COOLDOWN = 800 # miliseconds between shots

# Enemy's constants
E_SPRITE = "lib/game/sprites/enemy_ship/Ship6.png"
E_EXPLOSION = "lib/game/sprites/enemy_ship/explosion"
E_SCALE = (0, 0) # x and y

# Sounds
SOUNDS = "lib/game/sounds"

# API
API_URL = 'http://localhost:5000/json'