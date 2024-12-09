from ball import *
from bonus import *
from brick_field import *
from racket import *
from menu import *
from constants import *


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
        self.balls.append(Ball(self, screen))

        # Create a racket
        self.racket = Racket(self, screen)

    def update(self):
        """Run a \"Game tick\" Update object's position, read player input etc."""
        for b in self.balls:
            b.move()
        self.racket.move()

    def show_game(self):
        self.brick_field.show()
        for b in self.balls:
            b.show()
        self.racket.show()

    def show_menu(self):
        self.menu.show()

    def show(self):
        """Displays game on the screen"""
        # Show bricks
        # self.brick_field.show()
        # for b in self.balls:
        # b.show()
        if self.status == "menu":
            self.show_menu()
        elif self.status == "playing":
            self.update()
            self.show_game()
