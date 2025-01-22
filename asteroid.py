import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
       pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Split parameters
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_angle = random.uniform(20, 50)

        # Create split velocities
        velocity_1 = self.velocity.rotate(split_angle) * 1.2
        velocity_2 = self.velocity.rotate(-split_angle)

        # Create new asteroids
        pos_x, pos_y = self.position.x, self.position.y
        asteroid_1 = Asteroid(pos_x, pos_y, split_radius)
        asteroid_2 = Asteroid(pos_x, pos_y, split_radius)

        # Set velocities
        asteroid_1.velocity = velocity_1
        asteroid_2.velocity = velocity_2
