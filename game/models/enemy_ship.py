import pygame
from pygame.sprite import Sprite
from ..constants import E_SPRITE

class EnemyShip(Sprite):
    """ Defines the enemies' ships """
    def __init__(self, x_pos: int):
        super().__init__()
        image = pygame.image.load(E_SPRITE)
        self.image = pygame.transform.rotate(image, -90)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = 0
    
    def update(self) -> None:
        """ Moves the ship """
        self.rect.y += 3
        if self.rect.y > 960:
            self.kill()