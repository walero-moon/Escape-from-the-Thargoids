import pygame
import pygame.locals
from pygame.sprite import Sprite
from ..models.enemy_ship import EnemyShip

class EnemyController():
    """ Handles logic for enemies """
    def __init__(self, enemy):
        self._last_spawned = 0
        self.enemies = pygame.sprite.Group()
        self.enemies.add(enemy)

    def spawn(self):
        """ Handles enemy spawning logic """
        if (self._last_spawned + 1000) < pygame.time.get_ticks() and len(self.enemies) < 6:
            self._last_spawned = pygame.time.get_ticks()
            self._enemy = EnemyShip()
            self.enemies.add(self._enemy)