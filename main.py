import pygame # type: ignore
import constants
from player import Player

clock = pygame.time.Clock() # Creates a new clock object to track time
dt = 0  # initialize delta time to 0 seconds
player = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    game_loop(screen)

def game_loop(screen):
    while True:
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()