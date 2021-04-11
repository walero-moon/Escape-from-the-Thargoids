import pygame
import pygame.locals
import re
from ..views.menu import MainMenu

class MenuController():
    """ Handles the main menu for the game """
    def __init__(self, window):
        self._menu_view = MainMenu(window)
        self._last_selection = 'play'
        self.name = ''
    
    def update(self, keys):
        """ Changes selection on the menu """
        if self._last_selection == 'name_box_selected':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        self._last_selection = 'name_box'
                    elif event.key == 8:
                        self.name = self.name[0:-1] # For some reason we have to
                                                    # use -2 here. -1 doesn't work (???????)
                    else:
                        self.name += event.unicode if len(self.name) < 12 else ''
        # Up
        elif keys[pygame.locals.K_UP] or keys[pygame.locals.K_w]:
            self._last_selection = 'name_box'
        # Down
        elif keys[pygame.locals.K_DOWN] or keys[pygame.locals.K_s]:
            self._last_selection = 'play'
        # Right
        elif keys[pygame.locals.K_RIGHT] or keys[pygame.locals.K_d]:
            self._last_selection = 'exit'
        #Left
        elif keys[pygame.locals.K_LEFT] or keys[pygame.locals.K_a]:
            self._last_selection = 'play'
        # Selection handling
        elif keys[pygame.locals.K_z] or keys[pygame.locals.K_RETURN]:
            if self._last_selection == 'play':
                return True
            elif self._last_selection == 'exit':
                exit()
            elif self._last_selection == 'name_box':
                self._last_selection = 'name_box_selected'
        self._menu_view.update(self._last_selection, self.name)
        # print(self.name)
        