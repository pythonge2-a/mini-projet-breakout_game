import pygame

import constants as C
import numpy as np


class Animation_Break:
    """Class to handle brick destruction animations."""
    def __init__(self, position, size, color,number_of_fragments = C.ANIMATION_NUMBER_OF_FRAGMENTS,lifetime = C.ANIMATION_LIFETIME):
        self.particles = []
        self.lifetime = lifetime  # Duration of the animation in frames
        self.number_of_fragments = number_of_fragments  # Number of fragments
        # Generate particles
        for _ in range(self.number_of_fragments):  # Number of fragments
            particle = {
                "pos": np.array([position[0] + size[0] / 2, position[1] + size[1] / 2]),
                "vel": np.random.uniform(-3, 3, size=2),
                "color": color,
                "size": np.random.randint(2, 5),
            }
            self.particles.append(particle)

    def update(self):
        """Update particles' position and reduce lifetime."""
        if self.lifetime > 0:
            for particle in self.particles:
                particle["pos"] += particle["vel"]
                particle["size"] -= particle["size"] / self.lifetime
            self.lifetime -= 1
        else:
            del self  # Supprime explicitement l'objet

    def draw(self, screen):
        """Draw particles on the screen."""
        for particle in self.particles:
            pygame.draw.circle(screen, particle["color"], particle["pos"].astype(int), particle["size"])
