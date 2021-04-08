import pygame
from ..models.player import PlayerShip
from ..models.player_laser import PlayerLaser
from .player_controller import PlayerController
from ..models.enemy_ship import EnemyShip
from .enemy_controller import EnemyController
from ..constants import WIDTH, HEIGHT, P_SHOOT_COOLDOWN
from ..views.main_view import MainView

class GameController():
    """ Game's main controller """
    def __init__(self):
        pygame.init()
        # Game's window
        self._window = pygame.display.set_mode((WIDTH, HEIGHT))
        # Player instance
        self._player = PlayerShip()
        # Player's lasers
        self._player_controller = PlayerController(self._player)
        # Background art
        self._background = pygame.image.load("./game/sprites/background.png")
        # Clock
        self._clock = pygame.time.Clock()
        # Enemy
        self._first_enemy = EnemyShip()
        self._enemy_controller = EnemyController(self._first_enemy)

        # Views
        self._main_view = MainView(self._window, self._player, 
            self._player_controller.lasers, self._enemy_controller.enemies)

    def execute(self):
        """ Contains the game's main logic and loop """
        running = True
        while running:
            self._window.fill((0, 0, 0))
            self._clock.tick(60)

            # Closing the game
            for event in pygame.event.get():
                if event.type == pygame.locals.QUIT:
                    running = False

            # Player movement
            keys = pygame.key.get_pressed()
            self._player_controller.action(keys)

            # Enemies
            self._enemy_controller.spawn()

            for laser in self._player_controller.lasers:
                for enemy in self._enemy_controller.enemies:
                    if pygame.sprite.collide_mask(laser, 
                    enemy):
                        laser.kill()
                        enemy.kill()
            
            for enemy in self._enemy_controller.enemies:
                if pygame.sprite.collide_mask(self._player, enemy):
                    enemy.kill()

            self._enemy_controller.enemies.update()
            self._player_controller.lasers.update()
            # Update screen
            self._main_view.update()

if __name__ == "__main__":
    controller = GameController()
    controller.execute()