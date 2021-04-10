import os
import pygame
from pygame.sprite import Sprite
from ..constants import BACKGROUND

class Background(Sprite):
    """ Animates the background of the game """
    def __init__(self):
        super().__init__()
        self._sprites = []
        for sprite in os.listdir(BACKGROUND):
            sprite_img = pygame.image.load(f'{BACKGROUND}/{sprite}')
            self._sprites.append(sprite_img)

        self._current_sprite = 0
        self.image = self._sprites[self._current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self) -> None:
        """ Animates the background sprite """
        self._current_sprite += 1
        if self._current_sprite >= len(self._sprites):
            self._current_sprite = 0
        self.image = self._sprites[int(self._current_sprite)]