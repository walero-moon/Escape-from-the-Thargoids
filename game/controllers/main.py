import pygame
import pygame.locals
from ..models.player import PlayerShip
from ..models.player_laser import PlayerLaser
from .player_controller import PlayerController
from ..models.enemy_ship import EnemyShip
from ..constants import WIDTH, HEIGHT, P_SHOOT_COOLDOWN

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
        self._enemy_ship = EnemyShip(235)
        self._enemies = pygame.sprite.Group()
        self._enemies.add(self._enemy_ship)

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

            # Update screen
            self._player_controller.lasers.update()
            self._window.blit(self._background, (0, 0))
            self._player_controller.lasers.draw(self._window)
            self._window.blit(self._player.image, self._player.rect)
            self._enemies.update()
            self._enemies.draw(self._window)
            pygame.display.update()

if __name__ == "__main__":
    controller = GameController()
    controller.execute()