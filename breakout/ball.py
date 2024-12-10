import pygame
import brick_field
import racket
import constants as C
import numpy as np

"""class Ball:
    def __init__(self, screen, x, y, dx, dy, radius, color):
        self.screen = screen
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.radius = radius
        self.color = color
        
    def move(self, Racket, bricks):
        # Check if the ball hit the paddle
        if self.y + self.dy + self.radius >  Racket.height and self.x > Racket.x and self.x < Racket.x + Racket.width:
            self.dy = -self.dy       
        if self.y + self.dy - self.radius < self.sreen.get_height():
            self.dy = -self.dy
        if self.x + self.dx - self.radius < 0 or self.x + self.dx + self.radius > self.screen.get_width():
            self.dx = -self.dx
        if  self.y + self.dy - self.radius < 0:
            del(self)
        
        self.x += self.dx
        self.y += self.dy


    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

"""


class Ball:
    def __init__(
        self,
        breakout,
        screen,
        radius=C.BALL_RADIUS,
        color=C.BALL_COLOR,
        speed=C.BALL_SPEED,
        angle=None,
        positionX=C.BALL_START_X,
        positionY=C.BALL_START_Y,
    ):
        # Game attributs
        self.breakout = breakout
        self.screen = screen

        # Gemoetrical and graphical attributs
        self.pos = np.array([positionX, positionY])
        self.radius = radius
        self.color = color
        self.speed = speed

        # Start the ball to go up with a random angle
        # Generate a random angle between -pi and pi
        if angle is None:
            angle = np.random.uniform(-np.pi / 2, np.pi / 2)

        # Compute the vector components
        x = self.speed * np.cos(angle)
        y = self.speed * np.sin(angle)

        # Create the velocity vector
        self.vel = np.array([x, -y])

    def move(self):
        """Update ball position from velocity vector"""
        self.pos += self.vel
        # Check collisions
        self.check_colls(None, self.breakout.racket)

    def check_colls(self, brick_field, racket):
        """Check ball collisions"""
        # Define ball, racket symbols
        b_y = self.pos[1]
        b_x = self.pos[0]
        b_r = self.radius

        r_x = racket.pos[0]
        r_y = racket.pos[1]
        r_h = racket.size[1]
        r_w = racket.size[0]

        # Check racket collision
        if b_y + b_r > r_y and b_x + b_r > r_x and b_x < r_x + r_w:
            self.vel[1] *= -1

        # Check walls collision
        if b_y - b_r <= 0:
            self.vel[1] *= -1
        if b_x + b_r >= C.WINDOW_WIDTH or b_x + b_r <= 0:
            self.vel[0] *= -1
            
        if b_y + b_r >= C.WINDOW_HEIGHT:
            del self
            

    def show(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
