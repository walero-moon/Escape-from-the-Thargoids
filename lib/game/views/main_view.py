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

        # Font
        self._font_scores = pygame.font.SysFont("Dungeon", 20, bold=True)

        # Background animation
        self._background = Background()
        self._background_group = pygame.sprite.Group()
        self._background_group.add(self._background)
    
    def update(self, score: object):
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
        # Draw scores
        km = self._font_scores.render(f'Km: {score.km:.2f}', True, (255, 255, 255))
        kills = self._font_scores.render(f'Kills: {score.kills}', True, (255, 255, 255))
        total = self._font_scores.render(f'Total: {score.total}', True, (255, 255, 255))
        self._window.blit(total, (20, 20))
        self._window.blit(km, (20, 50))
        self._window.blit(kills, (20, 80))
        # Update display
        pygame.display.update()