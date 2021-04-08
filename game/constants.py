# This file will end up being huge, but that is to facilitate modifying
# player speed, projectile speed, projectile size, etc.


WIDTH = 550
HEIGHT = 900

# Player's constants
P_SPRITE = "game/sprites/player/player_ship.png"
P_SCALE = (80, 80) # Must be a tuple. (x, y)
P_LASER_SPRITES = "game/sprites/player/laser_sprites" # Relative to repo root
P_LASER_SCALE = (300, 0) # X and Y
P_SHOOT_COOLDOWN = 500 # miliseconds between shots

# Enemy's constants
E_SPRITE = "game/sprites/enemy_ship.png"
E_SCALE = (53, 90) # x and y
