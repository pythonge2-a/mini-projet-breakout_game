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
        self.brick_border_width = C.BRICK_BORDER_WIDTH
        pass

    def show(self):
        """Commentaire de fonction"""
        rect_position = (self.position, self.size)

        # Draws a rectangle to the screen
        pygame.draw.rect(self.screen, self.color, rect_position)
        pygame.draw.rect(
            self.screen,
            self.darken_color(self.color, C.BRICK_BORDER_COLOR_FACTOR),
            rect_position,
            width=self.brick_border_width,
        )

    def darken_color(self):
        print("Hey")
        pass


class Brick_field:
    """Define the field of bricks"""

    def __init__(self, screen):
        self.screen = screen
        # Create the brick array
        self.bricks = []

        # Generate bricks
        self.load_map(0)

    def show(self):
        for b in self.bricks:
            b.show()
        pass

    def load_map(self, map_index):
        """Load a map from the constants script."""
        map = C.LEVELS_MAPS[map_index]  # Save the map

        for i in range(C.BRICK_NB_BRICKS_Y):
            for j in range(C.BRICK_NB_BRICKS_X):
                # Compute brick position
                x = j * (C.BRICK_WIDTH + C.BRICK_HORIZONTAL_SPACING)
                y = i * (C.BRICK_HEIGHT + C.BRICK_VERTICAL_SPACING)
                x = j * (C.BRICK_WIDTH + C.BRICK_HORIZONTAL_SPACING)
                y = C.BRICK_TOP_CLEARANCE + i * (
                    C.BRICK_HEIGHT + C.BRICK_VERTICAL_SPACING
                )
                pos = [x, y]
                lives = int(map[i * C.BRICK_NB_BRICKS_X + j])
                # Add brick
                self.bricks.append(Brick(self.screen, pos, lives))
