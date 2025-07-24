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
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        # Should work??? Doesn't respond to my app close bind so I can't test :shrug:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #TODO: Probably replace this with return and do some cleaning up?
                sys.exit(0)

        screen.fill("#000000")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
