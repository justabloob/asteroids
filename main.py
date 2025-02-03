import pygame # type: ignore
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() # Creates a new clock object to track time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0  # initialize delta time to 0 seconds

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
        updatable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return

        screen.fill((0, 0, 0))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000 # limit the framerate to 60 FPS

if __name__ == "__main__":
    main()