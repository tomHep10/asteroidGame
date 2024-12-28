import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, position, radius):
        super().__init__(position.x, position.y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (250,250,250), self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        self.position += self.velocity * dt