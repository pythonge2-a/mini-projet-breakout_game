import pygame
import brick_field
import racket
import constants as C
import numpy as np


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
        self.check_colls(self.breakout.brick_field, self.breakout.racket)
        # rambow ball
        self.color = (
            np.sin(pygame.time.get_ticks() * 0.001 + 0) * 127 + 128,
            np.sin(pygame.time.get_ticks() * 0.001 + 2) * 127 + 128,
            np.sin(pygame.time.get_ticks() * 0.001 + 4) * 127 + 128,
        )

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
        if (
            b_y + b_r < r_y + r_h
            and b_y + b_r > r_y
            and b_x + b_r > r_x
            and b_x < r_x + r_w
        ):
            # Adjust the ball's velocity based on where it hit the racket
            self.vel[1] = -abs(self.vel[1])
            # Simplify the complex expression
            self.vel[0] += (b_x - r_x - r_w / 2) / (r_w / 2)
            # Normalize the velocity
            self.vel = (self.vel / np.linalg.norm(self.vel)) * self.speed


        # Check walls collision
        if b_y - b_r <= 0:
            self.vel[1] *= -1
        if b_x + b_r >= C.WINDOW_WIDTH or b_x - b_r <= 0:
            self.vel[0] *= -1

        if b_y - b_r >= C.WINDOW_HEIGHT:
            del self

        if brick_field != None:
            for brick in brick_field.bricks:
                brick_x = brick.position[0]
                brick_y = brick.position[1]
                brick_w = brick.size[0]
                brick_h = brick.size[1]
                if (
                    b_x + b_r > brick_x
                    and b_x - b_r < brick_x + brick_w
                    and b_y + b_r > brick_y
                    and b_y - b_r < brick_y + brick_h
                ):
                    # Check if the collision is vertical
                    if b_y - b_r < brick_y or b_y + b_r > brick_y + brick_h:
                        self.vel[1] *= -1
                    else:
                        self.vel[0] *= -1
                    if brick.lives > 0:
                        brick.lives -= 1
                        brick.color = C.BRICK_COLOR_MAP[brick.lives]
                    else:
                        brick_field.bricks.remove(brick)
                    break

    def show(self):

        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
