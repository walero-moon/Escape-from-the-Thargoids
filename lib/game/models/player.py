import pygame
import os
from pygame.sprite import Sprite
from ..constants import P_SPRITES

class PlayerShip(Sprite):
    """ Defines the player's ship """
    def __init__(self):
        super().__init__()
        self._sprites = []
        for sprite in os.listdir(P_SPRITES):
            sprite_img = pygame.image.load(f'{P_SPRITES}/{sprite}')
            sprite_img = pygame.transform.scale(sprite_img, (151, 100))
            self._sprites.append(sprite_img)

        self._current_sprite = 0
        self.image = self._sprites[self._current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = 235
        self.rect.y = 775
        self.rect.inflate_ip(0, -18)

    def update(self) -> None:
        """ Animates the background sprite """
        self._current_sprite += 0.2
        if self._current_sprite >= len(self._sprites):
            self._current_sprite = 0
        self.image = self._sprites[int(self._current_sprite)]
