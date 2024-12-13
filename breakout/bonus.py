import random as rd
import constants as C
from ball import *



# création des bonus/malus
class bolus:
    """Création des bonus et des malus"""

    def __init__(self, breakout, speed=C.BONUS_SPEED, brick = None, bonus = False, malus = False):
        self.breakout = breakout
        self.speed = speed
        self.y = brick.position[1]
        self.x = brick.position[0]
        self.brick = brick
        self.bonus = bonus
        self.malus = malus
        self.size = [C.BONUS_WIDTH, C.BONUS_HEIGHT]

        if self.bonus and not self.malus :
            self.bolus = self.set_bonus()
        elif not self.bonus and self.malus :
            self.bolus = self.set_malus()
        else :
            self.bolus = self.set_bolus()


        self.list_bonus = [
        self.grow_racket,
        self.grow_ball,
        self.speed_up_racket,
        self.speed_down_ball,
        self.add_ball,
        self.unstoppable,
        self.glu,
        self.break_brick,
        self.net
        ]
        self.list_malus = [
        self.speed_up_ball,
        self.speed_down_racket,
        self.shrink_racket,
        self.shrink_ball,
        self.reinforce_brick,
        self.ghost,
        self.reverse,
        self.explosion,
        self.unbreakable
        ]
        self.proba_bonus = [100, 50, 75, 75, 100, 5, 50, 25, 10]
        self.proba_malus = [100, 75, 75, 50, 75, 20, 25, 10, 5]

    def set_bonus(self):
        """Créé un bonus aléatoire"""

        bonus = rd.choices(self.list_bonus, self.proba_bonus)
        return bonus

    def set_malus(self):
        """Créé un malus aléatoire"""

        malus = rd.choices(self.list_malus, self.proba_malus)
        return malus

    def set_bolus(self):
        """Créé un malus ou un bonus aléatoire"""

        bolus = rd.choices(
            self.list_bonus + self.list_malus, self.proba_bonus + self.proba_malus
        )
        return bolus

    def move(self):
        """Déplacement du bonus/malus"""
        
        if self.y <= C.WINDOW_HEIGHT :
            self.y += self.speed
            if self.check_take() :
                self.bolus()    
        else :
            self.kill()     # est détruit en sortant de l'écran

    def check_take(self) :
        """Vérifie si le bonus est pris"""

        # position et taille du bonus/malus
        bm_x = self.x
        bm_y = self.y
        bm_h = self.size[1]
        bm_w = self.size[0]

        # position et taille de la raquette
        r_x = self.breakout.racket.x
        r_y = self.breakout.racket.y
        r_h = self.breakout.racket.paddle_height
        r_w = self.breakout.racket.paddle_width

        # vérifie si le bonus/malus est pris
        if (((bm_x - bm_w) < (r_x + r_w)) and ((bm_x + bm_w) > (r_x - r_w))) or (((bm_y - bm_h) < (r_y + r_h)) and ((bm_y + bm_h) > (r_y - r_h))) :
            return True
        else :
            return False

    def update(self) :
        """"met à jour l'état du bonus/malus"""

        if self.brick is None :
            self.move()

    def kill(self):
        """Détruit le bonus/malus"""

        del self

    def grow_racket(self) :
        """Bonus d'agrandissement de la raquette"""

        self.breakout.racket.paddle_width += 5
        pass

    def grow_ball(self) :
        """"Bonus d'agrandissement de la balle"""

        for b in self.breakout.balls :
            b.radius += 1 
        pass

    def speed_up_racket(self) :
        """Bonus d'accélération de la raquette"""

        self.breakout.racket.paddle_speed += 1
        pass

    def speed_down_ball(self) :
        """Bonus de ralentissement de la balle"""

        for b in self.breakout.balls :
            b.speed -= 1
        pass

    def add_ball(self) :
        """Bonus d'ajout d'une balle"""

        self.breakout.balls.append(Ball(self, self.breakout.screen))
        
        self.kill()

    def unstoppable(self) :
        """Bonus pour que la balle détruise tout sur son passage"""


        pass

    def glu(self) :
        """Bonus qui arrête la balle sur la raquette (lâche avec un bouton ou un temps)"""


        pass

    def break_brick(self) :
        """Bonus qui casse une brique aléatoire"""

        if len(self.breakout.brick_field.bricks) != 0 :
            brick_to_break = rd.choice(self.breakout.brick_field.bricks)

            brick_to_break.lives = 0

        self.kill()

    def net(self) :
        """Bonus qui empêche de perdre une bille"""


        pass

    def speed_up_ball(self) :
        """Malus d'accélération de la balle"""
        pass

    def speed_down_racket(self) :
        """Malus de ralentissement de la raquette"""

        self.breakout.racket.paddle_speed -= 1
        pass

    def shrink_racket(self) :
        """Malus de rétrécissement de la raquette"""

        self.breakout.racket.paddle_width -= 5
        pass

    def shrink_ball(self) :
        """Malus de rétrécissement de la balle"""

        for b in self.breakout.balls :
            b.radius -= 1
        pass

    def reinforce_brick(self) :
        """Malus d'ajout d'une vie à une brique"""

        if len(self.breakout.brick_field.bricks) != 0 :
            brick_to_reinforce = rd.choice(self.breakout.brick_field.bricks)

            brick_to_reinforce.lives += 1

        self.kill()

    def ghost(self) :
        """Malus qui empêche la balle de toucher les briques"""


        pass

    def reverse(self) :
        """Malus qui change les sens des contrôles"""


        pass

    def explosion(self) :
        """Malus qui rend des briques ou la balle explosive (vitesse de la bille augmente, angle change)"""


        pass

    def unbreakable(self) :
        """Malus qui rend une brique temporairement incassable"""


        pass
    

