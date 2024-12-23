import pygame
import brick_field
import racket
import constants as C
import numpy as np
import animation
from game_object import *
import random


class Ball(Game_object):
    def __init__(
        self,
        breakout,
        sprites,
        radius=C.BALL_RADIUS,
        color=C.BALL_COLOR,
        speed=C.BALL_SPEED,
        angle=None,
        position=np.array([C.BALL_START_X, C.BALL_START_Y]),
        coller=True,
    ):
        super().__init__(breakout, size=[0, 0], position=position, images=sprites)
        # Gemoetrical and graphical attributs
        self.radius = radius
        self.color = color
        self.speed = speed

        # Start the ball to go up with a random angle
        # Generate a random angle between -pi and pi
        if angle is None:
            angle = np.random.uniform(np.pi / 6, 5 * np.pi / 6)
        self.coller = coller

        # Compute the vector components
        x = self.speed * np.cos(angle)
        y = -self.speed * np.sin(angle)
        # Create the velocity vector
        self.velocity = np.array([x, y])

        # Load sprite
        self.load_sprite(C.TILESET_BALLS_POS, C.TILESET_BALLS_SIZE)


    def update(self):
        """Updates ball"""
        self.move()

        # met à jour la taille de la balle, je n'ai pas trouvé comment faire pour que 
        # l'image suive la position si la fonction pour changer la taille est appelée que
        # quand la balle change de taille
        self.change_size(self.position, [self.radius, self.radius]) 
        

    def move(self):
        """Update ball position from velocity vector"""
        if self.coller == True:
            self.position[0] = (
                self.breakout.racket.position[0] + self.breakout.racket.size[0] / 2
            )
            self.position[1] = self.breakout.racket.position[1] - self.radius
            if pygame.key.get_pressed()[pygame.K_UP]:
                self.coller = False
        else:
            # Check collisions
            self.check_colls(self.breakout.brick_field, self.breakout.racket)
            self.position += self.velocity

        # rambow ball
        self.color = (
            np.sin(pygame.time.get_ticks() * 0.001 + 0) * 127 + 128,
            np.sin(pygame.time.get_ticks() * 0.001 + 2) * 127 + 128,
            np.sin(pygame.time.get_ticks() * 0.001 + 4) * 127 + 128,
        )

    def check_colls(self, brick_field, racket):
        """Check ball collisions"""
        for other_ball in self.breakout.balls:
            if other_ball is self:
                continue
            if (
                np.linalg.norm(np.array(self.position) - np.array(other_ball.position))
                < self.radius + other_ball.radius
            ):
                # Calculate the normal vector
                epsilon = 1e-10
                normal = (np.array(self.position) - np.array(other_ball.position)) / (
                    np.linalg.norm(
                        np.array(self.position) - np.array(other_ball.position)
                    )
                    + epsilon
                )

                # Calculate the relative velocity
                relative_velocity = self.velocity - other_ball.velocity
                # Calculate the velocity along the normal
                velocity_along_normal = np.dot(relative_velocity, normal)
                # If the balls are moving apart, do nothing
                if velocity_along_normal > 0:
                    continue
                # Calculate the impulse scalar
                impulse = (
                    2
                    * velocity_along_normal
                    / (1 / self.radius + 1 / other_ball.radius)
                )
                # Apply the impulse to the velocities
                self.velocity -= impulse * normal / self.radius
                other_ball.velocity += impulse * normal / other_ball.radius

        # Define ball, racket symbols
        b_y = self.position[1]
        b_x = self.position[0]
        b_r = self.radius

        r_x = racket.position[0]
        r_y = racket.position[1]
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
            self.velocity[1] = -abs(self.velocity[1])
            # Simplify the complex expression
            self.velocity[0] += (b_x - r_x - r_w / 2) / (r_w / 2)
            # Normalize the velocity
            self.velocity = (self.velocity / np.linalg.norm(self.velocity)) * self.speed

        # Check walls collision
        if b_y - b_r <= 0:
            self.velocity[1] = abs(self.velocity[1])
        if b_x + b_r >= C.WINDOW_WIDTH:
            self.velocity[0] = -abs(self.velocity[0])
        if b_x - b_r <= 0:
            self.velocity[0] = abs(self.velocity[0])

        if b_y - b_r >= C.WINDOW_HEIGHT:
            self.breakout.Animation_Break.append(
                animation.Animation_Break(
                    self.position,
                    (self.radius, self.radius),
                    self.color,
                    number_of_fragments=300,
                )
            )
            if self.breakout.lives == 0 or len(self.breakout.balls) > 1:
                self.breakout.balls.remove(self)
            else:
                self.breakout.lives -= 1
                self.position[0] = (
                    self.breakout.racket.position[0] + self.breakout.racket.size[0] / 2
                )
                self.position[1] = self.breakout.racket.position[1] - self.radius
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
                    overlaps = {
                        "top": overlap_top,
                        "bottom": overlap_bottom,
                        "left": overlap_left,
                        "right": overlap_right,
                    }
                    min_overlap = min(overlaps.values())
                    min_sides = [
                        side
                        for side, overlap in overlaps.items()
                        if overlap == min_overlap
                    ]

                    # Ajuster la vitesse en fonction du côté
                    if "top" in min_sides:
                        self.velocity[1] *= -1  # Collision avec le haut de la brique
                    if "bottom" in min_sides:
                        self.velocity[1] *= -1  # Collision avec le bas de la brique
                    if "left" in min_sides:
                        self.velocity[
                            0
                        ] *= -1  # Collision avec le côté gauche de la brique
                    if "right" in min_sides:
                        self.velocity[
                            0
                        ] *= -1  # Collision avec le côté droit de la brique

                    # If the brick still has 1 life left at least
                    if brick.lives > 1:
                        # add animation
                        self.breakout.Animation_Break.append(
                            animation.Animation_Break(
                                brick.position,
                                brick.size,
                                brick.color,
                                number_of_fragments=30,
                            )
                        )
                        # Update lives and color
                        brick.lives -= 1

                        brick.color = C.BRICK_COLOR_MAP[brick.lives]
                        # Generate sprite
                        pos = [C.TILESET_BRICKS_POS[0] + (C.TILESET_BRICKS_SIZE[0] + 1 ) * (5 - brick.lives),  C.TILESET_BRICKS_POS[1] + (C.TILESET_BRICKS_SIZE[1] +1) * random.randint(0, 4)]
                        brick.load_sprite(pos, C.TILESET_BRICKS_SIZE)

                    else:
                        # Update points
                        self.breakout.score += brick.reward
                        
                        self.breakout.all_sprites.remove(brick)
                        brick_field.bricks.remove(brick)
                        # add animation
                        self.breakout.Animation_Break.append(
                            animation.Animation_Break(
                                brick.position, brick.size, brick.color
                            )
                        )
                        #'''je m'ammuse a rajouter des balles quand on casse une brique c'est fun mais pas très utile'''
                        # self.breakout.racket.size[0] += 500
                        # self.breakout.balls.append(Ball(self.breakout,self.sprites,coller=False,position=[self.position[0] + 2 * self.radius,self.position[1] + 2 * self.radius,],))

                    break
