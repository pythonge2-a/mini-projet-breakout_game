import random as rd
import constants as C


# création des bonus/malus
class bolus:
    """Création des bonus et des malus"""

    list_bonus = [
        "grow_racket",
        "grow_ball",
        "speed_up_racket",
        "speed_down_ball",
        "add_ball",
        "unstoppable",
        "glu",
        "break",
        "net",
    ]
    list_malus = [
        "speed_up_ball",
        "speed_down_racket",
        "shrink_racket",
        "shrink_ball",
        "reinforce_brick",
        "ghost",
        "reverse",
        "explosion",
        "unbreakable",
    ]
    proba_bonus = [100, 50, 75, 75, 100, 10, 25, 50, 10]
    proba_malus = [100, 75, 75, 50, 75, 20, 25, 10, 5]

    def __init__(self, speed=C.BONUS_SPEED, y=None, x=None):
        self.speed = speed
        self.y = y
        self.x = x

    def add_bonus(self):
        """Créé un bonus aléatoire"""

        bonus = rd.choices(self.list_bonus, self.proba_bonus)
        return bonus

    def add_malus(self):
        """Créé un malus aléatoire"""

        malus = rd.choices(self.list_malus, self.proba_malus)
        return malus

    def add_bolus(self):
        """Créé un malus ou un bonus aléatoire"""

        bolus = rd.choices(
            self.list_bonus + self.list_malus, self.proba_bonus + self.proba_malus
        )
        return bolus

    def move(self):
        """Déplacement du bonus/malus"""
        
        if self.y <= C.WINDOW_HEIGHT :
            self.y += self.speed
        else :
            self.kill()     # est détruit en sortant de l'écran

    def kill(self):
        """Détruit le bonus/malus"""
        del self
