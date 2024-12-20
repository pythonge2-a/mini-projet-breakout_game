import numpy as np
import pygame
import constants as C


class Game_object(pygame.sprite.Sprite):
    """Defines an object that is shown to the screen.
    It has everything that said object MUST contain.
    Nothing Less, nothing more.
    """

    def __init__(
        self,
        breakout,
        position: np.array,
        size: np.array,
        images: list,
        velocity: np.array = np.array([0, 0]),
        acceleration: np.array = np.array([0, 0]),
    ):
        # Initialize sprite
        super().__init__()
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
        self.sprites = images
        self.current_sprite = self.sprites[0]
        # Defines current sprite to show
        self.animation_index = 0
        self.animation_range = len(self.sprites)

        self.rect = (self.position, self.size)

    def move(self):
        """Move object, it's velocity, it's position"""
        self.velocity += self.acceleration
        self.position += self.velocity

    def update(self):
        """Update sprite"""
        self.animation_index += 1
        # Check animation index
        if self.animation_index >= self.animation_range:
            self.animation_index = 0
        # Modify sprite
        self.image = self.sprites[self.animation_index]

    def load_sprite(self, pos, size):
        """Load a sprite from the tileset"""
        tileset = pygame.image.load(C.TILESET_PATH).convert_alpha()
        rect = pygame.Rect(pos, size)
        self.image = tileset.subsurface(rect)
