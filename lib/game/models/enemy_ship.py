import pygame
from random import randint
from pygame.sprite import Sprite
from ..constants import E_SPRITE, E_SCALE
class EnemyShip(Sprite):
    """ Defines the enemies' ships """
    def __init__(self):
        super().__init__()
        image = pygame.image.load(E_SPRITE)
        self.image = pygame.transform.rotate(image, -90)
        self.image = pygame.transform.scale(self.image, E_SCALE)
        self.rect = self.image.get_rect()
        self.rect.x = randint(50, 470)
        self.rect.y = randint(-100, -10)
    
    def update(self) -> None:
        """ Moves the ship """
        self.rect.y += 3
        if self.rect.y > 960:
            self.kill()