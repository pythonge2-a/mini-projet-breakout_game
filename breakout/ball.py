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
    def __init__(self, breakout, screen):
        # Game attributs
        self.breakout = breakout
        self.screen = screen

        # Gemoetrical and graphical attributs
        self.pos = np.array([C.BALL_START_X, C.BALL_START_Y])
        self.radius = C.BALL_RADIUS
        self.color = C.BALL_COLOR
        self.speed = C.BALL_SPEED
        # Start the ball to go up
        self.vel = np.array([0, -self.speed])

    def move(self):
        """Update ball position from velocity vector"""
        self.pos += self.vel
        self.check_colls(None, self.breakout.racket)

    def check_colls(self, brick_field, racket):
        """Check ball collisions"""
        b_y = self.pos[1]
        b_x = self.pos[0]
        b_r = self.radius

        r_x = racket.pos[0]
        r_y = racket.pos[1]
        r_h = racket.size[1]
        r_w = racket.size[0]

        if b_y + 2 * b_r > r_y and b_x + 2 * b_r > r_x and b_x < r_x + r_w:
            self.vel[1] *= -1
        if b_y - b_r <= 0:
            self.vel[1] *= -1
        if b_x + 2 * b_r >= C.WINDOW_WIDTH or b_x <= 0:
            self.vel[0] *= -1

    def show(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
