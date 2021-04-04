import pygame
from pygame.sprite import Sprite

class PlayerLaser(Sprite):
    """ Projectile for the player's ship """
    def __init__(self, player_pos: tuple):
        super().__init__()
        image = pygame.image.load("game/sprites/player_laser.png")
        self.image = pygame.transform.rotate(image, 90)
        self.image = pygame.transform.scale(self.image, (13, 60))
        self.rect = self.image.get_rect()
        self.rect.x = player_pos[0] + 34
        self.rect.y = player_pos[1]
    
    def update(self):
        """ Moves the projectile """
        self.rect.y -= 15

        if self.rect.y < -60:
            self.kill()