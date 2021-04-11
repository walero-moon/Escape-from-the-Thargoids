import pygame
from random import randint
from pygame.sprite import Sprite
from ..constants import E_SPRITE, E_SCALE, WIDTH, HEIGHT
class EnemyShip(Sprite):
    """ Defines the enemies' ships """
    def __init__(self):
        super().__init__()
        image = pygame.image.load(E_SPRITE)
        self.image = pygame.transform.rotate(image, 180)
        # self.image = pygame.transform.scale(self.image, E_SCALE)
        self.rect = self.image.get_rect()
        self.rect.x = randint(WIDTH + 2 * self.rect[2], (WIDTH + 100) + 2 * self.rect[2])
        self.rect.y = randint(0, (HEIGHT + 100) - 2 * self.rect[3])
    
    def update(self) -> None:
        """ Moves the ship """
        self.rect.x -= 4
        if self.rect.x < -100:
            self.kill()