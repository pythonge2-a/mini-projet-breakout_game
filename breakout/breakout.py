from ball import *
from bonus import *
from brick_field import *
from racket import *
from menu import *
from constants import *


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

        # Create bonus list
        self.bonus_malus = []
        if len(self.bonus_malus) <= 0 :
            self.bonus_malus = self.add_bonus_malus()

    def update(self):
        """Run a \"Game tick\" Update object's position, read player input etc."""
        for b in self.balls:
            b.move()
        self.racket.move()
        #update bonus state
        for bo_ma in self.bonus_malus :
            bo_ma.update_bolus()

    def show_game(self):
        """Show the breakout game to the screen"""
        self.brick_field.show()
        for b in self.balls:
            b.show()
        self.racket.show()
        # Shows infos
        self.display_infos()

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

    def add_bonus_malus(self) :
        """add bonus or malus in bricks"""

        # à modifier, plusieurs bonus/malus peuvent être mis dans la même brique (et pas sûr du fonctionnement)
        bonus_malus = []
        for i in range(C.BONUS_QUANTITY) :
            brick_bonus_malus = rd.choice(self.brick_field.bricks)

            bonus_malus.append(bolus(screen=self.screen, breakout=self, brick=brick_bonus_malus, racket=self.racket))

        return bonus_malus


    
    

