import pygame
import pygame.locals
import re
from ..views.death import DeathView

class DeathController():
    """ Handles the death screen for the game """
    def __init__(self, window, score: object, api):
        self._death_view = DeathView(window, score)
        self._last_selection = 'upload'
        self._api_result = api
    
    def update(self, keys):
        """ Changes selection on the death screen """
        # Down
        if keys[pygame.locals.K_DOWN] or keys[pygame.locals.K_s]:
            self._last_selection = 'exit'
        # Up
        elif keys[pygame.locals.K_UP] or keys[pygame.locals.K_w]:
            self._last_selection = 'upload'
        # Selection handling
        elif keys[pygame.locals.K_z] or keys[pygame.locals.K_RETURN]:
            if self._last_selection == 'upload':
                return True
            elif self._last_selection == 'exit':
                exit()
        self._death_view.update(self._last_selection, self._api_result)
        # print(self.name)
        