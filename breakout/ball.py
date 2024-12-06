import pygame
import brick_field
import racket

class Ball:
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

