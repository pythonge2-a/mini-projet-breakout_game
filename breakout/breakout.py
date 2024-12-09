from ball import *
from bonus import *
from brick_field import *
from racket import *
from menu import *
from constants import *

# Constants


class Breakout:
    """Defines the breakout game."""

    def __init__(self, screen, font):
        # Define screen object
        self.screen = screen

        # Define menu
        self.menu = Menu(self, screen, font)
        # Define the field of bricks
        self.brick_field = Brick_field(screen)

        # Define the balls array
        self.balls = []

        # Defines game status
        self.status = "menu"

        # Define if game playing
        self.running = True
        # Create one ball
        # self.balls.append(Ball(screen))

        self.racket = Racket(screen, 200, 700)

    def show(self):
        """Displays game on the screen"""
        # Show bricks
        # self.brick_field.show()
        # for b in self.balls:
        # b.show()
        if self.status == "menu":
            self.menu.show()
        elif self.status == "playing":
            self.brick_field.show()
            for b in self.balls:
                b.show()
            self.racket.show()
