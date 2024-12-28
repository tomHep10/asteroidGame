import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    time = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    pl = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    A_f = AsteroidField()

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill((0,0,0))

        for updatables in updatable:
            updatables.update(dt)
        for drawables in drawable:
            drawables.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(pl):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        for shot in shots:
            shot.draw(screen)
            

        pygame.display.flip()
        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()