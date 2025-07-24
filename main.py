import pygame

from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, ASTEROID_KINDS, ASTEROID_SPAWN_RATE, ASTEROID_MAX_RADIUS


def main():
    pygame_module_status = pygame.init()
    signal.signal(signal.SIGQUIT, handle_sigquit)
    print(f"Successfully loaded {pygame_module_status[0]} pygame modules. {pygame_module_status[1]} modules failed to load.")
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    main_loop(screen)

def main_loop(screen):
    color = 0x000000
    while True:
        # Should work??? Doesn't respond to SIGQUIT so I can't test :shrug:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()

        screen.fill("#000000")
        pygame.display.flip()


if __name__ == "__main__":
    main()
