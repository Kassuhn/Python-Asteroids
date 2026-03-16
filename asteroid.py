import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        position = self.position
        pygame.draw.circle(screen, "white", position, LINE_WIDTH)

    def update(self, dt):
        position = self.position
        position += self.velocity * dt

    