import pygame
import constants as C
from game_object import *


class Racket(Game_object):
    """Define the user's racket"""

    def __init__(self, breakout, sprite=None):
        super().__init__(
            breakout,
            size=[C.RACKET_WIDTH, C.RACKET_HEIGHT],
            position=[C.RACKET_START_X, C.RACKET_START_Y],
            sprites=[sprite],
        )
        # Save special attributs
        self.color = C.RACKET_COLOR
        self.border_color = C.RACKET_BORDER_COLOR
        self.border_width = C.BRICK_BORDER_WIDTH
        self.speed = C.RACKET_SPEED

    def update(self):
        """Move the racket based on given players input"""
        x = self.position[0]
        width = self.size[0]
        # Check player's input, move the racket accordingly
        if pygame.key.get_pressed()[pygame.K_LEFT] and x > 0:
            self.position[0] -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT] and x < C.WINDOW_WIDTH - width:
            self.position[0] += self.speed

    def show(self):
        rect_position = (self.position, self.size)
        # Draws innner rectangle
        pygame.draw.rect(
            self.screen,
            self.color,
            rect_position,
            border_radius=C.RACKET_BORDER_RADIUS,
        )
        # Draws outer rectangle
        pygame.draw.rect(
            self.screen,
            self.border_color,
            rect_position,
            width=self.border_width,
            border_radius=C.RACKET_BORDER_RADIUS,
        )
