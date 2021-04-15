import pygame
from .background import Background
from ..constants import WIDTH, HEIGHT, FONT

class DeathView():
    """ Death for the game """
    def __init__(self, window, score: object):
        self._selection_colour = (255, 111, 0)
        self._window = window
        # Fonts
        self._font_title = pygame.font.Font(FONT, 48, bold=True)
        self._font_btns = pygame.font.Font(FONT, 36, bold=True)
        self._font_player = pygame.font.Font(FONT, 34, bold=True)
        self._font_scores = pygame.font.Font(FONT, 20, bold=True)
        # Texts
        self._title = self._font_title.render("You died", True, (255, 255, 255))
        # Score
        self._km = score.km
        self._total = score.total
        self._kills = score.kills
        # self._kill_score = scores[killScore]
        self._km = self._font_scores.render(f'Kms flown: {self._km}', True, (255, 255, 255))
        self._total = self._font_scores.render(f'Total score: {self._total}', True, (255, 255, 255))
        self._kills = self._font_scores.render(f'Total kills: {self._kills}', True, (255, 255, 255))

        self._background = Background()
        self._background_group = pygame.sprite.Group()
        self._background_group.add(self._background)
    
    def update(self, selection, api):
        """ Updates the main menu screen """
        play_text = None
        exit_text = None
        if selection == 'upload':
            play_text = self._font_btns.render("Upload results", True, self._selection_colour)
        else:
            play_text = self._font_btns.render("Upload results", True, (255, 255, 255))

        if selection == 'exit':
            exit_text = self._font_btns.render("Exit", True, self._selection_colour)
        else:
            exit_text = self._font_btns.render("Exit", True, (255, 255, 255))
        # Background
        self._background_group.update()
        self._background_group.draw(self._window)

        # You lost
        position_x = int((WIDTH / 2) - (self._title.get_rect()[2] / 2))
        self._window.blit(self._title, (position_x, 200))

        # Score
        self._window.blit(self._total, (position_x + 20, 350))
        self._window.blit(self._km, (position_x + 20, 380))
        self._window.blit(self._kills, (position_x + 20, 410))

        # Upload
        if selection == 'upload':
            pygame.draw.rect(self._window, self._selection_colour, 
            ((position_x - 48), 500, 340, 70), width=5, border_radius=4)
        else:
            pygame.draw.rect(self._window, (255, 255, 255), 
            ((position_x - 48), 500, 340, 70), width=5, border_radius=4)
        self._window.blit(play_text, ((position_x - 40) + 20, 511))

        # Exit
        if selection == 'exit':
            pygame.draw.rect(self._window, (self._selection_colour), 
            ((position_x + 60), 590, 122, 70), width=5, border_radius=4)
        else:
            pygame.draw.rect(self._window, (255, 255, 255), 
            ((position_x + 60), 590, 122, 70), width=5, border_radius=4)
        self._window.blit(exit_text, ((position_x + 67) + 20, 601))

        self._window.blit(api, (480, 850))
        pygame.display.update()



