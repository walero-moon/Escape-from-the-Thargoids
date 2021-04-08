import pygame
from pygame.sprite import Sprite
from ..constants import P_LASER_WIDTH as WIDTH
from ..constants import P_LASER_HEIGHT as HEIGHT
from ..constants import P_LASER_SPRITE as SPRITE

class PlayerLaser(Sprite):
    """ Projectile for the player's ship """
    def __init__(self, player_pos: tuple):
        super().__init__()
        image = pygame.image.load(SPRITE)
        self.image = pygame.transform.rotate(image, 90)
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = player_pos[0] + 34
        self.rect.y = player_pos[1]
    
    def update(self) -> None:
        """ Moves the projectile """
        self.rect.y -= 15

        if self.rect.y < -60:
            self.kill()