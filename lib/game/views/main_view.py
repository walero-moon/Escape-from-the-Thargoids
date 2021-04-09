import pygame
from ..constants import BACKGROUND
from .background import Background

class MainView():
    """ Main view of the game. Renders """
    def __init__(self, window, player, p_lasers, enemies):
        self._window = window

        # Player
        self._player = player
        self._p_lasers = p_lasers
        self._enemies = enemies

        # Background animation
        self._background = Background()
        self._background_group = pygame.sprite.Group()
        self._background_group.add(self._background)
    
    def update(self):
        """ Updates the entire game window """
        # Background
        self._background_group.update()
        self._background_group.draw(self._window)
        # Draw lasers
        self._p_lasers.draw(self._window)
        # Draw player
        self._player.update()
        self._window.blit(self._player.image, self._player.rect)
        # Draw enemies
        self._enemies.draw(self._window)
        # Update display
        pygame.display.update()