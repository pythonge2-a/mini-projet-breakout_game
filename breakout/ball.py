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
        coller = True
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
            angle = np.random.uniform(np.pi/6, 5*np.pi/6)
        self.coller = coller

        # Compute the vector components
        x = self.speed * np.cos(angle)
        y = -self.speed * np.sin(angle)
        # Create the velocity vector
        self.vel = np.array([x, y])
        

    def move(self):
        """Update ball position from velocity vector"""
        if(self.coller == True):
            self.pos[0] = self.breakout.racket.pos[0] + self.breakout.racket.size[0]/2
            self.pos[1] = self.breakout.racket.pos[1] - self.radius
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.coller = False
        else:   
            # Check collisions
            self.check_colls(self.breakout.brick_field, self.breakout.racket)
            self.pos += self.vel

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
            if self.breakout.lives  == 0 or len(self.breakout.balls) > 1:
                self.breakout.balls.remove(self)
            else:
                self.breakout.lives -= 1
                self.pos[0] = self.breakout.racket.pos[0] + self.breakout.racket.size[0]/2
                self.pos[1] = self.breakout.racket.pos[1] - self.radius
                self.coller = True

        if brick_field != None:
            # Goes through each brick of the field
            for brick in brick_field.bricks:
                # Compute position values
                brick_x = brick.position[0]
                brick_y = brick.position[1]
                brick_w = brick.size[0]
                brick_h = brick.size[1]
                # If brick collision
                if (
                    b_x + b_r > brick_x
                    and b_x - b_r < brick_x + brick_w
                    and b_y + b_r > brick_y
                    and b_y - b_r < brick_y + brick_h
                ):
                    # Calcul des distances pour déterminer le côté de la collision
                    overlap_top = abs(b_y + b_r - brick_y)
                    overlap_bottom = abs(b_y - b_r - (brick_y + brick_h))
                    overlap_left = abs(b_x + b_r - brick_x)
                    overlap_right = abs(b_x - b_r - (brick_x + brick_w))

                    # Trouver le côté avec la plus petite distance d'overlap
                    min_overlap = min(
                        overlap_top, overlap_bottom, overlap_left, overlap_right
                    )

                    # Ajuster la vitesse en fonction du côté
                    if min_overlap == overlap_top:
                        self.vel[1] *= -1  # Collision avec le haut de la brique
                    elif min_overlap == overlap_bottom:
                        self.vel[1] *= -1  # Collision avec le bas de la brique
                    elif min_overlap == overlap_left:
                        self.vel[0] *= -1  # Collision avec le côté gauche de la brique
                    elif min_overlap == overlap_right:
                        self.vel[0] *= -1  # Collision avec le côté droit de la brique

                    # If the brick still has 1 life left at least
                    if brick.lives > 1:
                        # Update lives and color
                        brick.lives -= 1
                        brick.color = C.BRICK_COLOR_MAP[brick.lives]
                    else:
                        # Update points
                        self.breakout.score += brick.reward
                        brick_field.bricks.remove(brick) 
                        '''je m'ammuse a rajouter des balles quand on casse une brique c'est fun mais pas très utile'''
                        #self.breakout.balls.append(Ball(self.breakout, self.screen, coller = False, positionX = self.pos[0], positionY = self.pos[1]))
   
                    break

    def show(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
