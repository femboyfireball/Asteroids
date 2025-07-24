import sys

import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS
from player import Player


def main():
    pygame_module_status = pygame.init()
    print(f"Successfully loaded {pygame_module_status[0]} pygame modules. {pygame_module_status[1]} modules failed to load.")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_loop(screen)

def main_loop(screen):

    game_clock = pygame.time.Clock()
    dt = 0

    updateables = pygame.sprite.Group()
    renderables = pygame.sprite.Group()

    Player.containers = (updateables, renderables)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        # Close the game when pygame detects a QUIT event. Doesn't work under some circumstances
        # such as Hyprland's ctrl + q.
        # TODO: Fix that considering I use Hyprland. Keyboard interrupts are a jank solution
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # TODO: Probably replace this with return and do some cleaning up?
                sys.exit(0)

        # TODO: Possibly split into "Update Sprites", "Update Screen", and "Render" methods?
        screen.fill("#000000")

        for updateable in updateables:
            updateable.update(dt)
        for renderable in renderables:
            renderable.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
