import pygame
import constants as C

def main():
    pygame.init()
    pygame.display.set_mode((C.SCREEN_WIDTH, C.SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        surface = pygame.display.get_surface()
        surface.fill("black")
        pygame.display.flip()
    print("Starting asteroids!")
    print(f"Screen width: {C.SCREEN_WIDTH}")
    print(f"Screen height: {C.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
