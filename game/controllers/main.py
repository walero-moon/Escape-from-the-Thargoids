import pygame
import pygame.locals
from ..models.player import PlayerShip
from ..models.player_laser import PlayerLaser
from pygame.sprite import Sprite

def main():
    pygame.init()
    window = pygame.display.set_mode((550, 900))
    clock = pygame.time.Clock()

    player = PlayerShip()
    background = pygame.image.load("./game/sprites/background.png")
    player_lasers = pygame.sprite.Group()

    last_fire = 0
    cooldown = 500 # miliseconds

    running = True
    while running:
        window.fill((0, 0, 0))
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT]:
            player.rect.x = min(player.rect.x + 5, 470)
        if keys[pygame.locals.K_LEFT]:
            player.rect.x = max(player.rect.x - 5, 0)
        if keys[pygame.locals.K_UP]:
            player.rect.y = max(player.rect.y - 5, 0)
        if keys[pygame.locals.K_DOWN]:
            player.rect.y = min(player.rect.y + 5, 820)

        # Shooting projectile
        if keys[pygame.locals.K_SPACE]:
            current_ticks = pygame.time.get_ticks()
            if current_ticks > last_fire + cooldown:
                last_fire = current_ticks
                laser = PlayerLaser((player.rect.x, player.rect.y))
                player_lasers.add(laser)

        player_lasers.update()
        window.blit(background, (0, 0))
        player_lasers.draw(window)
        window.blit(player.image, player.rect)
        pygame.display.update()