from ball import *
from bonus import *
from brick_field import *
from racket import *
from menu import *
from constants import *

from animation import *


class Breakout:
    """Defines the breakout game."""

    def __init__(self, screen, font):
        # Score
        self.score = 0
        self.level = 0
        self.lives = C.GAME_START_LIVES

        # Define screen object
        self.screen = screen
        self.font = font
        # Define menu
        self.menu = Menu(self, screen, font)
        # Define the field of bricks
        self.brick_field = Brick_field(self)

        # Define the balls array
        self.balls = []

        # Defines game status
        self.status = "menu"

        # Define if game playing
        self.running = True
        # Create one ball
        self.balls.append(Ball(self, [None]))
        # Create a racket
        self.racket = Racket(self, [None])

        # Sprite's lists
        self.all_sprites = pygame.sprite.Group()

        # Create bonus list
        self.bonus_malus = []
        if len(self.bonus_malus) <= 0:
            self.bonus_malus = self.add_bonus_malus()
        self.Animation_Break = []

        # Add bricks to sprites list
        for b in self.brick_field.bricks:
            self.all_sprites.add(b)
        # Add ball to sprites list
        self.all_sprites.add(self.balls[0])

        # Add racket
        self.all_sprites.add(self.racket)

    def update(self):
        """Run a \"Game tick\" Update object's position, read player input etc."""
        if self.balls == []:
            self.status = "game_over"
        else:
            for b in self.balls:
                b.update()

        self.racket.update()
        # update bonus state
        for bo_ma in self.bonus_malus:
            bo_ma.update_bolus()
        if self.Animation_Break != []:
            for anim in self.Animation_Break:
                anim.update()

    def show_game(self):
        """Show the breakout game to the screen"""
        # Shows infos
        self.display_infos()

        if self.Animation_Break != []:
            # Dessiner les animations en cours
            for anim in self.Animation_Break:
                anim.draw(self.screen)

        self.all_sprites.draw(self.screen)

    def show_menu(self):
        self.menu.show()

    def show(self):
        """Displays game on the screen"""
        if self.status == "menu":
            self.show_menu()
        elif self.status == "playing":
            self.update()
            self.show_game()
        elif self.status == "game_over":
            self.show_game_over()

    def display_infos(self):
        """Shows score, lives, level"""
        self.display_score()
        self.display_lives()
        self.display_level()

    def display_score(self):
        """Displays score"""

        # Define text
        score_txt = self.font.render(f"Score:{self.score}", True, SCORE_FONT_COLOR)

        c_x = C.SCORE_RECT_X
        c_y = C.SCORE_RECT_Y

        # Define rectangle
        score_rec = score_txt.get_rect(topleft=(c_x, c_y))
        self.screen.blit(score_txt, score_rec)

    def display_level(self):
        """Writes level"""
        # Define text
        level_txt = self.font.render(f"Level:{self.level}", True, LEVEL_FONT_COLOR)

        c_x = C.LEVEL_RECT_X
        c_y = C.LEVEL_RECT_Y

        # Define rectangle
        level_rec = level_txt.get_rect(topright=(c_x, c_y))
        self.screen.blit(level_txt, level_rec)

    def display_lives(self):
        """Shows lives"""
        # Define text
        lives_txt = self.font.render(f"Lives:{self.lives}", True, LIVES_FONT_COLOR)

        c_x = C.LIVES_RECT_X
        c_y = C.LIVES_RECT_Y

        # Define rectangle
        lives_rec = lives_txt.get_rect(topleft=(c_x, c_y))
        self.screen.blit(lives_txt, lives_rec)
        pass

    def add_bonus_malus(self):
        """add bonus or malus in bricks"""

        # si le nombre de bonus/malus ne dépasse pas le nombre de briques, il n'y aura qu'un bonus/malus par brique
        bonus_malus = []
        i = 0
        if len(self.brick_field.bricks) >= C.BONUS_QUANTITY:
            brick_bonus_malus = rd.sample(self.brick_field.bricks, C.BONUS_QUANTITY)
        else:
            brick_bonus_malus = [
                rd.choice(self.brick_field.bricks) for x in range(C.BONUS_QUANTITY)
            ]

        for brick in brick_bonus_malus:

            bonus_malus.append(
                Bolus(
                    breakout=self,
                    sprites=[None],
                    brick=brick,
                    racket=self.racket,
                )  
            )
            self.all_sprites.add(bonus_malus[i])
            i += 1

        return bonus_malus

    def show_game_over(self):
        """Show game over screen"""
        # rambow ball
        color = (
            np.sin(pygame.time.get_ticks() * 0.001 + 0) * 127 + 128,
            np.sin(pygame.time.get_ticks() * 0.001 + 2) * 127 + 128,
            np.sin(pygame.time.get_ticks() * 0.001 + 4) * 127 + 128,
        )
        # Define text
        game_over_txt = self.font.render("Game Over", True, color)

        # Define rectangle
        game_over_rec = game_over_txt.get_rect(
            center=(C.WINDOW_WIDTH / 2, C.WINDOW_HEIGHT / 2)
        )
        self.screen.blit(game_over_txt, game_over_rec)

        pass
