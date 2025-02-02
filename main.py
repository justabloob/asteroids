import pygame # type: ignore
import constants

clock = pygame.time.Clock()
dt = 0  # initialize delta time to 0 seconds

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_loop(screen)

def game_loop(screen):
    while True:
        screen.fill((0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()