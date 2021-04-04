import pygame
from pygame.sprite import Sprite

class PlayerShip(Sprite):
    """ Defines the player's ship """

    def __init__(self):
        super().__init__()
        image = pygame.image.load("game/sprites/player_ship.png")
        self.image = pygame.transform.scale(image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = 235
        self.rect.y = 775

