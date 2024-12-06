import pygame
import numpy as np
import random


class Brick:
    """Commentaire de classe"""

    def __init__(self, screen, position, size):
        # Screen object
        self.screen = screen
        # Define the brick dimensions
        self.position = position
        self.size = size

        self.color = "blue"
        pass

    def show(self):
        """Commentaire de fonction"""
        rect_position = (self.position, self.size)
        # Draws a rectangle to the screen
        pygame.draw.rect(self.screen, self.color, rect_position)


class Brick_field:
    """Define the field of bricks"""

    def __init__(self, screen):
        self.screen = screen
        # Create the brick array
        self.bricks = []

        # Generate random bricks everywhere
        for i in range(100):
            # Genreate random position
            position = np.array([random.random() * 800, random.random() * 600])
            # Generate random size
            size = np.array([random.random() * 30, random.random() * 30])
            self.bricks.append(Brick(screen, position, size))
        pass

    def show(self):
        for b in self.bricks:
            b.show()
        pass
