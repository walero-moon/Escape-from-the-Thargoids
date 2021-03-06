import pygame
import os
from pygame.sprite import Sprite
from ..constants import P_LASER_SPRITES as SPRITES

class PlayerLaser(Sprite):
    """ Projectile for the player's ship """
    def __init__(self, player_pos: tuple):
        super().__init__()
        self._sprites = []
        for sprite in os.listdir(SPRITES):
            sprite_img = pygame.image.load(f'{SPRITES}/{sprite}')
            sprite_img = pygame.transform.scale2x(sprite_img)
            self._sprites.append(sprite_img)

        self._current_sprite = 0
        self.image = self._sprites[self._current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = player_pos[0] + 120
        self.rect.y = player_pos[1] + 70
    
    def update(self) -> None:
        """ Moves the projectile and updates the sprite"""
        # movement
        self.rect.x += 20
        if self.rect.x > 1600:
            self.kill()

        # animation
        self._current_sprite += 0.3
        if self._current_sprite >= len(self._sprites):
            self._current_sprite = 1
        self.image = self._sprites[int(self._current_sprite)]