from constants import *
import pygame

def main():
    pygame.init()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    new_clock = pygame.time.Clock()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        BLACK = 0, 0, 0
        screen.fill(BLACK)
        pygame.display.flip()


        elapsed_time = new_clock.tick(60)
        dt = elapsed_time / 1000

if __name__ == "__main__":
    main()