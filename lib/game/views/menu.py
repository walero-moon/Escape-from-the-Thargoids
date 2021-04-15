import pygame
from .background import Background
from ..constants import WIDTH, HEIGHT, FONT

class MainMenu():
    """ Starting menu for the game """
    def __init__(self, window):
        self._selection_colour = (255, 111, 0)
        self._window = window
        # Fonts
        self._font_title = pygame.font.Font(FONT, 48, bold=True)
        self._font_btns = pygame.font.Font(FONT, 36, bold=True)
        self._font_controls = pygame.font.Font(FONT, 20, bold=True)
        self._font_player = pygame.font.Font(FONT, 34, bold=True)
        # Texts
        self._title = self._font_title.render("Escape from the Thargoids", True, (255, 255, 255))
        controls = 'Use the Arrow keys or WASD to move. Press Z or K to fire. Press enter to select.'
        self._controls = self._font_controls.render(controls, True, (255, 255, 255))
        self._background = Background()
        self._background_group = pygame.sprite.Group()
        self._background_group.add(self._background)
    
    def update(self, selection, name):
        """ Updates the main menu screen """
        play_text = None
        exit_text = None
        if selection == 'play':
            play_text = self._font_btns.render("Play", True, self._selection_colour)
        else:
            play_text = self._font_btns.render("Play", True, (255, 255, 255))

        if selection == 'exit':
            exit_text = self._font_btns.render("Exit", True, self._selection_colour)
        else:
            exit_text = self._font_btns.render("Exit", True, (255, 255, 255))
        # Background
        self._background_group.update()
        self._background_group.draw(self._window)

        # Title
        position_x = int((WIDTH / 2) - (self._title.get_rect()[2] / 2))
        self._window.blit(self._title, (position_x, 200))

        # Play
        if selection == 'play':
            pygame.draw.rect(self._window, self._selection_colour, 
            (position_x + 180, 500, 126, 70), width=5, border_radius=4)
        else:
            pygame.draw.rect(self._window, (255, 255, 255), 
            (position_x + 180, 500, 126, 70), width=5, border_radius=4)
        self._window.blit(play_text, (position_x + 200, 511))

        # Exit
        if selection == 'exit':
            pygame.draw.rect(self._window, (self._selection_colour), 
            ((2 * position_x) - 55, 500, 114, 70), width=5, border_radius=4)
        else:
            pygame.draw.rect(self._window, (255, 255, 255), 
            ((2 * position_x) - 55, 500, 114, 70), width=5, border_radius=4)
        self._window.blit(exit_text, ((2 * position_x - 55) + 20, 511))
        # Blits controls
        self._window.blit(self._controls, (290, 850))

        # Blitting name
        player = self._font_player.render(name, True, (255, 255, 255))
        player_rec_x = player.get_rect()[2]
        position_player = (WIDTH / 2) - (player_rec_x / 2)
        if selection =='name_box':
            editing = self._font_controls.render('Press enter to start editing player name',
            True, self._selection_colour)
            player = self._font_player.render(name, True, self._selection_colour)
            pygame.draw.line(self._window, self._selection_colour, (565, 450), (1000, 450))
            self._window.blit(editing, (WIDTH/2 - 246, 365))
        elif selection == 'name_box_selected':
            editing = self._font_controls.render('Editing name. Press \'ESC\' to confirm name',
            True, self._selection_colour)
            player = self._font_player.render(name, True, self._selection_colour)
            pygame.draw.line(self._window, self._selection_colour, (565, 450), (1000, 450))
            self._window.blit(editing, (WIDTH/2 - 240, 365))
        else:
            editing = self._font_controls.render('Select me to edit your name',
            True, (255, 255, 255))
            player = self._font_player.render(name, True, (255, 255, 255))
            pygame.draw.line(self._window, (255, 255, 255), (565, 450), (1000, 450))
            self._window.blit(editing, (WIDTH/2 - 170, 365))
        self._window.blit(player, (position_player - 20, 400))

        pygame.display.update()



