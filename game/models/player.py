import pygame
from pygame.sprite import Sprite
from ..constants import P_SPRITE, P_SCALE

class PlayerShip(Sprite):
    """ Defines the player's ship """
    def __init__(self):
        super().__init__()
        image = pygame.image.load(P_SPRITE)
        self.image = pygame.transform.scale(image, P_SCALE)
        self.rect = self.image.get_rect()
        self.rect.x = 235
        self.rect.y = 775

