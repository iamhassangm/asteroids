import pygame
from asteroid import Asteroid
import constants as C
from player import Player
from shot import Shot
from asteroidfield import AsteroidField


def main():
    pygame.init()
    screen = pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(C.SCREEN_WIDTH/2, C.SCREEN_HEIGHT/2)
    AsteroidField()

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.is_collision(player):
                print("Game Over!")
                exit()
        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()

        dt = clock.tick(60) / 1000


    print("Starting asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
