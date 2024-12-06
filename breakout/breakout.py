from ball import *
from bonus import *
from brick_field import *
from racket import *
from menu import *


class Breakout:
    """Defines the breakout game."""

    def __init__(self, screen, font):
        # Define menu
        self.menu = Menu(screen, font)
        # Define screen object
        self.screen = screen
        # Define the field of bricks
        self.brick_field = Brick_field(screen)

        # Define the balls array
        self.balls = []

        # Create one ball
        self.balls.append(Ball(screen))
        pass

    def show(self):
        """Displays game on the screen"""
        # Show bricks
        # self.brick_field.show()
        # for b in self.balls:
        # b.show()
        self.menu.show()
        pass
