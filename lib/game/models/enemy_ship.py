import pygame
import os
from random import randint
from pygame.sprite import Sprite
from ..constants import E_SPRITE, E_SCALE, WIDTH, HEIGHT, E_EXPLOSION

EXPLOSION_SPRITES = []
for sprite in os.listdir(E_EXPLOSION):
    sprite_img = pygame.image.load(f'{E_EXPLOSION}/{sprite}')
    EXPLOSION_SPRITES.append(sprite_img)
class EnemyShip(Sprite):
    """ Defines the enemies' ships """
    def __init__(self):
        super().__init__()
        image = pygame.image.load(E_SPRITE)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(WIDTH + 2 * self.rect[2], (WIDTH + 100) + 2 * self.rect[2])
        self.rect.y = randint(0, (HEIGHT + 100) - 2 * self.rect[3])
        self._kill = False

        self._current_e_sprite = 0
    
    def update(self) -> None:
        """ Moves the ship """
        if self._kill:
            self._current_e_sprite += 0.3
            self.rect.x -= 4

            if self._current_e_sprite >= len(EXPLOSION_SPRITES):
                super().kill()
                
            if self._current_e_sprite >= len(EXPLOSION_SPRITES):
                self._current_e_sprite = 1
            self.image = EXPLOSION_SPRITES[int(self._current_e_sprite)]
            return None
        self.rect.x -= 4
        if self.rect.x < -300:
            super().kill()
    
    def kill(self):
        """ Animates the explosion of the ship """
        # animation
        self._kill = True