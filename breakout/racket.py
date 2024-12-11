import pygame
import constants as C


class Racket:
    def __init__(self, breakout, screen,paddle_width = C.RACKET_WIDTH, paddle_height = C.RACKET_HEIGHT, paddle_color = C.RACKET_COLOR, paddle_speed = C.RACKET_SPEED, x = C.RACKET_START_X, y = C.RACKET_START_Y,color_border = C.RACKET_BORDER_COLOR, border_width = C.RACKET_BORDER_WIDTH):
        # Game attributs
        self.breakout = breakout
        self.screen = screen

        # Gemoetrical and graphical attributs
        self.pos = [x, y]
        self.size = [paddle_width, paddle_height]
        self.color = paddle_color
        self.border_color = color_border
        self.border_width = border_width
        self.speed = paddle_speed

    def move(self):
        """Move the racket based on given players input"""
        x = self.pos[0]
        width = self.size[0]
        # Check player's input, move the racket accordingly
        if pygame.key.get_pressed()[pygame.K_LEFT] and x > 0:
            self.pos[0] -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT] and x < C.WINDOW_WIDTH - width:
            self.pos[0] += self.speed

    def show(self):
        rect_position = (self.pos, self.size)
        # Draws innner rectangle
        pygame.draw.rect(
            self.screen,
            self.color,
            rect_position,
            border_radius=C.RACKET_BORDER_RADIUS,
        )
        # Draws outer rectangle
        pygame.draw.rect(
            self.screen,
            self.border_color,
            rect_position,
            width=self.border_width,
            border_radius=C.RACKET_BORDER_RADIUS,
        )
