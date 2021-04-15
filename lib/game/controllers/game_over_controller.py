import pygame
import pygame.locals
import re
from ..views.death import DeathView
from ..constants import SOUNDS

class DeathController():
    """ Handles the death screen for the game """
    def __init__(self, window, score: object, api):
        # Music
        self._menu_music = pygame.mixer.music.load(f'{SOUNDS}/in-the-wreckage.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        # Select noise
        self._select_sound = pygame.mixer.Sound(f'{SOUNDS}/select.mp3')
        self._select_sound.set_volume(0.5)
        self._sound_delay = 0
        self._death_view = DeathView(window, score)
        self._last_selection = 'upload'
        self._api_result = api
    
    def update(self, keys):
        """ Changes selection on the death screen """
        # Down
        if keys[pygame.locals.K_DOWN] or keys[pygame.locals.K_s]:
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
            self._last_selection = 'exit'
        # Up
        elif keys[pygame.locals.K_UP] or keys[pygame.locals.K_w]:
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
            self._last_selection = 'upload'
        # Selection handling
        elif keys[pygame.locals.K_z] or keys[pygame.locals.K_RETURN]:
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
            if self._last_selection == 'upload':
                return True
            elif self._last_selection == 'exit':
                exit()
        self._death_view.update(self._last_selection, self._api_result)
        # print(self.name)
        