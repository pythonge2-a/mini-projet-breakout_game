import pygame
import numpy as np
import random
import constants as C
from game_object import Game_object


class Brick(Game_object):
    """Commentaire de classe"""

    def __init__(self, breakout, sprites, position: np.array, lives, sprite=None):
        super().__init__(
            breakout=breakout,
            position=position,
            images=sprites,
            size=[C.BRICK_WIDTH, C.BRICK_HEIGHT],
        )
        # Screen object
        # Define the brick dimensions
        self.lives = lives
        self.color = C.BRICK_COLOR_MAP[self.lives]
        self.brick_border_width = C.BRICK_BORDER_WIDTH

        # Define score as its own lives
        self.reward = lives

        # Generate sprite
        self.load_sprite(C.TILESET_BRICKS_POS, C.TILESET_BRICKS_SIZE)
    
    def show(self):
        """Commentaire de fonction"""
        """rect_position = (self.position, self.size)

        # Draws the inner rectangle
        pygame.draw.rect(self.screen, self.color, rect_position)
        # Draws the outer rectangle
        pygame.draw.rect(
            self.screen,
            self.darken_color(self.color, C.BRICK_BORDER_COLOR_FACTOR),
            rect_position,
            width=self.brick_border_width,
        )"""
        super().show()

    def darken_color(self, color, factor):
        """Return a darker color version"""
        return tuple(max(0, min(int(c * factor), 255)) for c in color)


class Brick_field:
    """Define the field of bricks"""

    def __init__(self, breakout):
        self.breakout = breakout
        # Create the brick array
        self.bricks = []

        # Generate map
        self.load_map(0)

    def update(self):
        """Updates brick field"""
        for b in self.bricks:
            b.update()

    def show(self):
        # Shows bricks
        for b in self.bricks:
            b.show()

    def load_map(self, map_index):
        """Load a map from the constants script."""
        map = C.LEVELS_MAPS[map_index]  # Save the map

        # Goes through all the bricks
        for i in range(C.BRICK_NB_BRICKS_Y):
            for j in range(C.BRICK_NB_BRICKS_X):
                # Compute brick position
                x = j * (C.BRICK_WIDTH + C.BRICK_HORIZONTAL_SPACING)
                y = i * (C.BRICK_HEIGHT + C.BRICK_VERTICAL_SPACING)

                # Add top clearance
                y += C.BRICK_TOP_CLEARANCE
                pos = [x, y]

                # Get corresponding brick lives (map)
                lives = int(map[i * C.BRICK_NB_BRICKS_X + j])
                # Add brick
                self.bricks.append(Brick(self.breakout, [None], pos, lives))
