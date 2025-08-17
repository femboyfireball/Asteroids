import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        raise NotImplementedError("Subclass did not implement CircleShape.draw")

    def update(self, dt):
        # sub-classes must override
        raise NotImplementedError("Subclass did not implement CircleShape.update")

    def is_colliding(self, other_circle):
        distance = pygame.math.Vector2.distance_to(self.position, other_circle.position)
        if (self.radius + other_circle.radius) > distance:
            return True
        else:
            return False
