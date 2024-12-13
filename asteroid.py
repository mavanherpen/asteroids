import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # overriding parent draw method
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    # overriding parent update method
    def update(self, dt):
        self.position += self.velocity * dt