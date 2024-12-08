import pygame
import numpy as np
import random
import constants as C


class Brick:
    """Commentaire de classe"""

    def __init__(self, screen, position, lives):
        # Screen object
        self.screen = screen
        # Define the brick dimensions
        self.position = position
        self.lives = lives
        self.size = [C.BRICK_WIDTH, C.BRICK_HEIGHT]

        self.color = C.BRICK_COLOR_MAP[self.lives]
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

        # Generate bricks
        for i in range(C.BRICK_NB_BRICKS_Y):
            for j in range(C.BRICK_NB_BRICKS_X):
                # Compute brick position
                x = j * C.BRICK_WIDTH
                y = i * C.BRICK_HEIGHT
                pos = [x, y]
                lives = np.random.randint(0, C.BRICK_MAX_LIVES)
                # Add brick
                self.bricks.append(Brick(self.screen, pos, lives))

    def show(self):
        for b in self.bricks:
            b.show()
        pass
