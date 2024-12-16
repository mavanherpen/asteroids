import pygame
import random
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
    
    # adding a splitting method:
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vector_new_1 = self.velocity.rotate(random_angle)
            vector_new_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = vector_new_1 * 1.2
            
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = vector_new_2 * 1.2
