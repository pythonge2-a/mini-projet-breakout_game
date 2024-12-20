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
            images=[sprite],
        )
        # Save special attributs
        self.color = C.RACKET_COLOR
        self.border_color = C.RACKET_BORDER_COLOR
        self.border_width = C.BRICK_BORDER_WIDTH
        self.speed = C.RACKET_SPEED

        # Load sprite
        self.load_sprite(C.TILESET_RACKETS_POS, C.TILESET_RACKETS_SIZE)

    def update(self):
        """Move the racket based on given players input"""
        x = self.position[0]
        width = self.size[0]
        # Check player's input, move the racket accordingly
        if pygame.key.get_pressed()[pygame.K_LEFT] and x > 0:
            self.position[0] -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT] and x < C.WINDOW_WIDTH - width:
            self.position[0] += self.speed
