import pygame
import pygame.locals
import re
from ..views.menu import MainMenu
from ..constants import SOUNDS

class MenuController():
    """ Handles the main menu for the game """
    def __init__(self, window):
        # Music
        self._menu_music = pygame.mixer.music.load(f'{SOUNDS}/loading.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        # Select noise
        self._select_sound = pygame.mixer.Sound(f'{SOUNDS}/select.mp3')
        self._select_sound.set_volume(0.5)
        self._sound_delay = 0
        self._menu_view = MainMenu(window)
        self._last_selection = 'play'
        self.name = ''
    
    def update(self, keys):
        """ Changes selection on the menu """
        if self._last_selection == 'name_box_selected':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        if self._sound_delay < pygame.time.get_ticks():
                            self._sound_delay = pygame.time.get_ticks() + 200
                            self._select_sound.play()
                        self._last_selection = 'name_box'
                    elif event.key == 8:
                        self.name = self.name[0:-1] # For some reason we have to
                                                    # use -2 here. -1 doesn't work (???????)
                    else:
                        self.name += event.unicode if len(self.name) < 12 else ''
        # Up
        elif keys[pygame.locals.K_UP] or keys[pygame.locals.K_w]:
            self._last_selection = 'name_box'
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
        # Down
        elif keys[pygame.locals.K_DOWN] or keys[pygame.locals.K_s]:
            self._last_selection = 'play'
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
        # Right
        elif keys[pygame.locals.K_RIGHT] or keys[pygame.locals.K_d]:
            self._last_selection = 'exit'
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
        #Left
        elif keys[pygame.locals.K_LEFT] or keys[pygame.locals.K_a]:
            self._last_selection = 'play'
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
        # Selection handling
        elif keys[pygame.locals.K_z] or keys[pygame.locals.K_RETURN]:
            if self._sound_delay < pygame.time.get_ticks():
                self._sound_delay = pygame.time.get_ticks() + 200
                self._select_sound.play()
            if self._last_selection == 'play':
                return True
            elif self._last_selection == 'exit':
                exit()
            elif self._last_selection == 'name_box':
                self._last_selection = 'name_box_selected'
        self._menu_view.update(self._last_selection, self.name)
        # print(self.name)
        