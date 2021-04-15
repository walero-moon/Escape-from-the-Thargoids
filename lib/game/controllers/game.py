import pygame
import requests

from ..constants import WIDTH, HEIGHT, P_SHOOT_COOLDOWN, API_URL, SOUNDS
# Player
from ..models.player import PlayerShip
from ..models.player_laser import PlayerLaser
from .player_controller import PlayerController
# Enemies
from ..models.enemy_ship import EnemyShip
from .enemy_controller import EnemyController
# Views
from ..views.main_view import MainView
from .menu_controller import MenuController
from .game_over_controller import DeathController
# Score
from ...models.score import Score
from ...models.score_manager import ScoreManager

class GameController():
    """ Game's main controller """
    def __init__(self):
        pygame.init()
        # Game's window
        self._window = pygame.display.set_mode((WIDTH, HEIGHT))
        # Menu
        self._menu = MenuController(self._window)
        # Player instance
        self._player = PlayerShip()
        # Player's lasers
        self._player_controller = PlayerController(self._player)
        # Clock
        self._clock = pygame.time.Clock()
        # Enemy
        self._first_enemy = EnemyShip()
        self._enemy_controller = EnemyController(self._first_enemy)
        # Score
        self._score = Score()
        self._score_manager = ScoreManager()
        # Views
        self._main_view = MainView(self._window, self._player, 
            self._player_controller.lasers, self._enemy_controller.enemies)
        self._menu_controller = MenuController(self._window)
        self._death_created = False

        # Sounds and music
        self._main_music_playing = False
        self._explosion_sound = pygame.mixer.Sound(f'{SOUNDS}/explosion.mp3')
        self._explosion_sound.set_volume(0.2)

        self._state = 'menu'
        self._sent = False
        font = pygame.font.SysFont("Dungeon", 20, bold=True)
        self._api_result = font.render('', True, (255, 255, 255))
    
    def menu(self):
        """ Menu logic """
        self._window.fill((0, 0, 0))
        self._clock.tick(60)
        keys = pygame.key.get_pressed()
        if self._menu_controller.update(keys):
            self._state = 'game'
            if self._menu_controller.name == '':
                self._score.name = 'Unknown'
            else:
                self._score.name = self._menu_controller.name
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exit()
    
    def game(self):
        """ Game's main loop """
        self._score.km = round(pygame.time.get_ticks() / 1000, 2)
        self._window.fill((0, 0, 0))
        self._clock.tick(60)

        if not self._main_music_playing:
            self._main_music = pygame.mixer.music.load(f'{SOUNDS}/battle.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            self._main_music_playing = True
        # Closing the game
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exit()

        # Player movement
        keys = pygame.key.get_pressed()
        self._player_controller.action(keys)
        # Enemies
        self._enemy_controller.spawn()

        for laser in self._player_controller.lasers:
            for enemy in self._enemy_controller.enemies:
                if pygame.sprite.collide_mask(laser, enemy):
                    # Increase scores
                    self._score.kills += 1
                    self._score.kill_score += 1

                    self._explosion_sound.play()

                    laser.kill()
                    enemy.kill()
        
        for enemy in self._enemy_controller.enemies:
            if pygame.sprite.collide_mask(self._player, enemy):
                self._score_manager.add_score(self._score)
                self._score_manager.save()
                self._state = 'dead'

        self._enemy_controller.enemies.update()
        self._player_controller.lasers.update()
        # Update screen
        self._main_view.update(self._score)
    
    def exit(self):
        """ Death screen logic """
        if self._death_created == False:
            self._death_controller = DeathController(self._window, self._score, self._api_result)
            self._death_created = True
        self._window.fill((0, 0, 0))
        self._clock.tick(60)
        keys = pygame.key.get_pressed()
        if self._death_controller.update(keys):
            # Sending to API
            if self._sent == False:
                font = pygame.font.SysFont("Dungeon", 20, bold=True)
                try:
                    requests.put(f"{API_URL}", json=self._score.json)
                    self._api_result = font.render(f'Successfully uploaded score',
                        True, (255, 255, 255))
                except:
                    self._api_result = font.render(f'Failed to upload. Server currently offline. Sorry',
                        True, (255, 0, 0))
                self._death_controller = DeathController(self._window, self._score, self._api_result)
                self._sent = True
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                exit()
        
        self._window.blit(self._api_result, (290, 850))

    def execute(self):
        """ Contains the game's main logic and loop """
        running = True
        while running:
            if self._state == 'menu':
                self.menu()
            elif self._state == 'game':
                self.game()
            elif self._state == 'dead':
                self.exit()

if __name__ == "__main__":
    controller = GameController()
    controller.execute()