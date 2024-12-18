import numpy as np
import pygame


class Game_object:
    """Defines an object that is shown to the screen.
    It has everything that said object MUST contain.
    Nothing Less, nothing more.
    """

    def __init__(
        self,
        breakout,
        position: np.array,
        size: np.array,
        sprites: list,
        velocity: np.array = np.array([0, 0]),
        acceleration: np.array = np.array([0, 0]),
    ):
        # Defines references
        self.breakout = breakout
        self.screen = breakout.screen

        # Defines physical properties
        self.position = position
        self.size = size
        self.velocity = velocity
        self.acceleration = acceleration

        # Defines graphical properties (sprites)
        # Defines the different sprites for this object (useful to animate said object)
        self.sprites = sprites
        self.current_sprite = self.sprites[0]
        # Defines current sprite to show
        self.animation_index = 0
        self.animation_range = len(self.sprites)

    def update(self):
        """Updates object, it's animation, it's position"""
        self.velocity += self.acceleration
        self.position += self.velocity

    def update_animation(self):
        """Udpate sprite"""
        self.animation_index += 1
        # Check animation index
        if self.animation_index == self.animation_range:
            self.animation_index = 0
        # Modify sprite
        self.current_sprite = self.sprites[self.animation_index]

    def show(self):
        """Displays game object on the screen"""
        pass
