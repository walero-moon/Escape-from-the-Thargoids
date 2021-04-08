import pygame
from ..constants import BACKGROUND

class MainView():
    """ Main view of the game. Renders """
    def __init__(self, window, player, p_lasers, enemies):
        self._window = window
        self._player = player
        self._p_lasers = p_lasers
        self._enemies = enemies
        self._background = pygame.image.load(BACKGROUND)
    
    def update(self):
        """ Updates the entire game window """
        # Set background image
        self._window.blit(self._background, (0, 0))
        # Draw lasers
        self._p_lasers.draw(self._window)
        # Draw player
        self._window.blit(self._player.image, self._player.rect)
        # Draw enemies
        self._enemies.draw(self._window)
        # Update display
        pygame.display.update()