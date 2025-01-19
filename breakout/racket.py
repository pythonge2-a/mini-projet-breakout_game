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
        self.border_width = C.RACKET_BORDER_WIDTH
        self.speed = C.RACKET_SPEED
        self.reverse = False
        self.auto_mode = False
        self.invisible = False
        self.load_invisible = False

        # Load sprite
        self.load_sprite(C.TILESET_RACKETS_POS, C.TILESET_RACKETS_SIZE)

        # copy size
        self.previous_width = self.size[0]

    def update(self):
        """Move the racket based on given players input"""
        x = self.position[0]
        width = self.size[0]

        # met à jour la taille de la raquette, je n'ai pas trouvé comment faire pour que
        # l'image suive la position si la fonction pour changer la taille est appelée que
        # quand la raquette change de taille
        self.change_size(self.position, self.size)

        # Check player's input, move the racket accordingly
        if self.reverse and not self.auto_mode:
            if pygame.key.get_pressed()[pygame.K_RIGHT] and x > 0:
                self.position[0] -= self.speed
            if pygame.key.get_pressed()[pygame.K_LEFT] and x < C.WINDOW_WIDTH - width:
                self.position[0] += self.speed
        elif self.auto_mode:
            if (self.breakout.balls[0].position[0] < C.WINDOW_WIDTH - width / 2) and (
                self.breakout.balls[0].position[0] > width / 2
            ):
                self.position[0] = self.breakout.balls[0].position[0] - (
                    self.size[0] / 2
                )
        else:
            if pygame.key.get_pressed()[pygame.K_LEFT] and x > 0:
                self.position[0] -= self.speed
                if self.invisible and not self.load_invisible:
                    self.load_sprite(C.TILESET_INVISIBLE_POS, C.TILESET_RACKETS_SIZE)
                    self.load_invisible = True
            if pygame.key.get_pressed()[pygame.K_RIGHT] and x < C.WINDOW_WIDTH - width:
                self.position[0] += self.speed
                if self.invisible and not self.load_invisible:
                    self.load_sprite(C.TILESET_INVISIBLE_POS, C.TILESET_RACKETS_SIZE)
                    self.load_invisible = True

            if (
                not pygame.key.get_pressed()[pygame.K_RIGHT]
                and not pygame.key.get_pressed()[pygame.K_LEFT]
                and self.invisible
            ):
                self.load_sprite(C.TILESET_RACKETS_POS, C.TILESET_RACKETS_SIZE)
                self.load_invisible = False
