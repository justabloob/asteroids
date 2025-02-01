import pygame
import constants

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: " + str(constants.SCREEN_WIDTH))
    print("Screen height: " + str(constants.SCREEN_HEIGHT))
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

def game_loop():
    while True:
        pygame.Surface.fill((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, 0))
        pygame.display.flip()

if __name__ == "__main__":
    main()