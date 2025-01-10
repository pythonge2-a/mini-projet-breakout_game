import random as rd
import constants as C
from ball import *


# création des bonus/malus
class Bolus(Game_object):
    """Création des bonus et des malus"""

    def __init__(
        self,
        breakout,
        sprites,
        racket,
        speed=C.BONUS_SPEED,
        brick=None,
        bonus=False,
        malus=False,
        sprite=None,
    ):
        super().__init__(
            breakout,
            position=np.array(
                [brick.position[0] + C.BONUS_POS_X, brick.position[1] + C.BONUS_POS_Y]
            ),
            size=np.array(
                [C.BONUS_WIDTH, C.BONUS_HEIGHT],
            ),
            images=sprites,
        )
        self.racket = racket
        self.speed = speed
        self.brick = brick
        self.bonus = bonus
        self.malus = malus
        self.use = False
        self.end = False
        self.start = False
        self.count = 0
        self.unbrickable = None
        self.net_sprite = None

        self.list_bonus = [
            [self.grow_racket, 1],
            [self.grow_ball, 0],
            [self.speed_up_racket, 6],
            [self.speed_down_ball, 7],
            [self.add_ball, 2],
            [self.unstoppable, 3],
            [self.glu, 4],
            [self.break_brick, 5],
            [self.net, 8],
        ]
        self.list_malus = [
            [self.speed_up_ball, 12],
            [self.speed_down_racket, 13],
            [self.shrink_racket, 11],
            [self.shrink_ball, 10],
            [self.reinforce_brick, 14],
            [self.ghost, 15],
            [self.reverse, 16],
            [self.explosion, 17],
            [self.unbreakable, 18],
        ]
        self.proba_bonus = [100, 50, 75, 75, 100, 5, 100, 30, 10]
        self.proba_malus = [100, 75, 75, 50, 75, 10, 50, 50, 10]

        if self.bonus and not self.malus:
            self.bolus = self.set_bonus()
        elif not self.bonus and self.malus:
            self.bolus = self.set_malus()
        else:
            self.bolus = self.set_bolus()

        pos = [
            C.TILESET_BONUSES_POS[0],
            C.TILESET_BONUSES_POS[1] + (C.TILESET_BONUSES_SIZE[1] + 1) * self.bolus[0][1],
        ]

        self.load_sprite(pos, C.TILESET_BONUSES_SIZE)

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

    def move_bolus(self):
        """Déplacement du bonus/malus"""

        if (self.position[1] <= C.WINDOW_HEIGHT) and not self.end:
            if not self.use:
                self.position[1] += self.speed
                # vérifie si le bonus est pris
                if self.check_take():
                    self.use = True
        else:
            self.kill()  # est détruit en sortant de l'écran

    def check_take(self):
        """Vérifie si le bonus est pris"""

        # position et taille du bonus/malus
        bm_x = self.position[0]
        bm_y = self.position[1]
        bm_h = self.size[1]
        bm_w = self.size[0]

        # position et taille de la raquette
        r_x = self.racket.position[0]
        r_y = self.racket.position[1]
        r_h = self.racket.size[1]
        r_w = self.racket.size[0]

        # vérifie si le bonus/malus est pris
        if (((bm_x) < (r_x + r_w)) and ((bm_x + bm_w) > (r_x))) and (
            ((bm_y + bm_h) < (r_y + r_h)) and ((bm_y + bm_h) > (r_y))
        ):
            return True
        else:
            return False

    def update_bolus(self):
        """met à jour l'état du bonus/malus"""

        # déplacement du bonus/malus quand une brique est détruite
        if len(self.brick.groups()) == 0:
            self.move_bolus()

        # quand un bonus est pris, son affichage disparaît
        if self.use:
            self.breakout.all_sprites.remove(self)
            self.count_ticks()
        else:
            self.count = 0

    def count_ticks(self):
        """Active le bonus et compte le temps où il est actif"""

        self.count += 1
        # active le bonus
        self.bolus[0][0]()

    def kill(self):
        """Détruit le bonus/malus"""

        # enlève l'affichage du bonus/malus
        self.breakout.all_sprites.remove(self)
        del self

    def grow_racket(self):
        """Bonus d'agrandissement de la raquette"""

        # quand le bonus est pris la raquette est agrandie
        if not self.start:
            self.start = True
            self.racket.size[0] += C.RACKET_GROW_SIZE
        # au bout d'un temps donné, la raquette reprend sa taille précédente
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            if self.racket.size[0] > C.RACKET_GROW_SIZE:
                self.racket.size[0] -= C.RACKET_GROW_SIZE
            self.use = False

    def grow_ball(self):
        """ "Bonus d'agrandissement de la balle"""

        # quand le bonus est pris toutes les balles affichées grandissent
        if not self.start:
            self.start = True
            for b in self.breakout.balls:
                b.radius += C.BALL_GROW_SIZE
        # après le temps d'activation, les balles qui ont été agrandie rétrécissent
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            for b in self.breakout.balls:
                if b.radius > C.BALL_RADIUS:
                    b.radius -= C.BALL_GROW_SIZE
            self.use = False

    def speed_up_racket(self):
        """Bonus d'accélération de la raquette"""

        # la vitesse de la raquette augmente quand le bonus est pris
        if not self.start:
            self.start = True
            self.racket.speed += C.RACKET_SPEED_UP
        # après le temps d'activation la raquette ralenti
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            if self.racket.speed > C.RACKET_SPEED_UP:
                self.racket.speed -= C.RACKET_SPEED_UP
            self.end = True
            self.use = False

    def speed_down_ball(self):
        """Bonus de ralentissement de la balle"""

        # quand le bonus est récupéré, les balles affichées ralentissent
        if not self.start:
            self.start = True
            for b in self.breakout.balls:
                if b.speed > C.BALL_SPEED_DOWN:
                    b.speed -= C.BALL_SPEED_DOWN
        # au bout d'un temps donné, les balles qui ont été ralentie accélèrent
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            for b in self.breakout.balls:
                if b.speed < C.BALL_SPEED:
                    b.speed += C.BALL_SPEED_DOWN
            self.use = False

    def add_ball(self):
        """Bonus d'ajout d'une balle"""

        if not self.start:
            # une balle est créé
            self.breakout.balls.append(
                Ball(
                    self.breakout,
                    self.sprites,
                    coller=False,
                    position=[C.BALL_START_X, C.BALL_START_Y],
                )
            )
            self.breakout.all_sprites.add(
                self.breakout.balls[len(self.breakout.balls) - 1]
            )  # ajoute le sprite de la dernière balle de la liste
            self.start = True
            self.use = False
            self.end = True

    def unstoppable(self):
        """Bonus pour que la balle détruise tout sur son passage"""

        if not self.start:
            self.start = True
            # le bonus ne fonctionne que sur une balle, la première de la liste
            self.breakout.balls[0].unstoppable = True
            self.end = True
            self.use = False

    def glu(self):
        """Bonus qui arrête la balle sur la raquette (lâche avec un bouton)"""

        # quand le bonus est récupéré, la balle se colle à la raquette quand elle la touche
        if not self.start:
            self.start = True
            for b in self.breakout.balls:
                # si une modification de la balle est active, le bonus ne s'active pas
                if not b.unstoppable and not b.ghost:
                    b.glu = True
                    # charge le sprite de la balle collante
                    b.load_sprite(C.TILESET_GLU_POS, C.TILESET_BALLS_SIZE)
            self.end = True
            self.use = False

    def break_brick(self):
        """Bonus qui casse une brique aléatoire"""

        if not self.start:
            # choisi une brique aléatoire
            if len(self.breakout.brick_field.bricks) != 0:
                brick_to_break = rd.choice(self.breakout.brick_field.bricks)

            # détruit la brique et ajoute les points de sa destruction
            self.breakout.score += brick_to_break.reward
            self.breakout.all_sprites.remove(brick_to_break)
            self.breakout.brick_field.bricks.remove(brick_to_break)
            # add animation
            self.breakout.Animation_Break.append(
                animation.Animation_Break(
                    brick_to_break.position, brick_to_break.size, brick_to_break.color
                )
            )

            self.start = True
            self.use = False
            self.end = True

    def net(self):
        """Bonus qui empêche de perdre une bille"""

        rebounds = 0
        # toutes les balles affichées ne peuvent plus disparaître
        for b in self.breakout.balls:
            if not b.net:
                b.net = True
            else:
                # le nombre de rebonds est compté
                rebounds += b.count_net
        # affiche l'image du filet
        if self.net_sprite is None:
            self.net_sprite = Net(breakout=self.breakout, sprites=[None])
            self.breakout.all_sprites.add(self.net_sprite)
        # après un nombre de rebond donné, le filet disparaît
        if (rebounds >= C.NET_REBOUNDS) and not self.end:
            self.end = True
            self.net_sprite.kill()
            for b in self.breakout.balls:
                b.net = False
                b.count_net = 0
            self.use = False

    def speed_up_ball(self):
        """Malus d'accélération de la balle"""

        # quand le malus est récupéré, toutes les balles affichées accélèrent
        if not self.start:
            self.start = True
            for b in self.breakout.balls:
                b.speed += C.BALL_SPEED_UP
        # au bout d'un temps d'activation, toutes les balles accélérées sont ralenties
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            for b in self.breakout.balls:
                if b.speed > C.BALL_SPEED:
                    b.speed -= C.BALL_SPEED_UP
            self.use = False

    def speed_down_racket(self):
        """Malus de ralentissement de la raquette"""

        # quand le malus est récupéré, la raquette ralenti
        if not self.start:
            self.start = True
            if self.racket.speed > C.RACKET_SPEED_DOWN:
                self.racket.speed -= C.RACKET_SPEED_DOWN
        # après un temps d'activation la raquette accélère
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            self.racket.speed += C.RACKET_SPEED_DOWN
            self.use = False

    def shrink_racket(self):
        """Malus de rétrécissement de la raquette"""

        # la raquette est rétrécie quand le malus est pris
        if not self.start:
            self.start = True
            if self.racket.size[0] > C.RACKET_SHRINK_SIZE:
                self.racket.size[0] -= C.RACKET_SHRINK_SIZE
        # après un temps donné, la raquette grandis
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            self.racket.size[0] += C.RACKET_SHRINK_SIZE
            self.use = False

    def shrink_ball(self):
        """Malus de rétrécissement de la balle"""

        # toutes les balles affichées sont rétrécie
        if not self.start:
            self.start = True
            for b in self.breakout.balls:
                if b.radius > C.BALL_SHRINK_SIZE:
                    b.radius -= C.BALL_SHRINK_SIZE
        # après un temps d'activation, les balles rétrécies sont agrandie
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            for b in self.breakout.balls:
                if b.radius < C.BALL_RADIUS:
                    b.radius += C.BALL_SHRINK_SIZE
            self.use = False

    def reinforce_brick(self):
        """Malus d'ajout d'une vie à une brique"""

        # une brique aléatoire est renforcée si le malus est pris
        if not self.start:
            # choisi une brique aléatoire
            brick_to_reinforce = rd.choice(self.breakout.brick_field.bricks)
            # ajoute une vie a la brique choisie
            if brick_to_reinforce.lives < C.BRICK_MAX_LIVES:
                brick_to_reinforce.lives += C.BRICK_ADD_LIFE
                # Generate sprite
                pos = [
                    C.TILESET_BRICKS_POS[0],
                    C.TILESET_BRICKS_POS[1]
                    + (C.TILESET_BRICKS_SIZE[1] + 1) * (5 - (brick_to_reinforce.lives)),
                ]
                # met à jour le sprite
                brick_to_reinforce.load_sprite(pos, C.TILESET_BRICKS_SIZE)

            self.start = True
            self.use = False
            self.end = True

    def ghost(self):
        """Malus qui empêche la balle de toucher les briques"""

        # la balle passe par dessus les briques sans les casser si le malus est pris
        if not self.start:
            self.start = True
            # le malus ne fonctionne que sur une balle, la première de la liste
            self.breakout.balls[0].ghost = True
            self.end = True
            self.use = False

    def reverse(self):
        """Malus qui change les sens des contrôles"""

        # inverse les commande si le malus est pris
        if not self.start:
            self.start = True
            self.racket.reverse = True
            self.racket.load_sprite(C.TILESET_REVERSE_POS, C.TILESET_RACKETS_SIZE)
        # après un temps donné, les contrôles reviennent à la normale
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.racket.reverse = False
            self.racket.load_sprite(C.TILESET_RACKETS_POS, C.TILESET_RACKETS_SIZE)
            self.end = True
            self.use = False

    def explosion(self):
        """Malus qui rend des briques ou la balle explosive (vitesse de la bille augmente, angle change)
        quand les balles touchent les briques, la vitesse change"""

        # quand le malus est récupéré, toutes les balles deviennent explosive
        if not self.start:
            self.start = True
            for b in self.breakout.balls:
                if not b.explosion:
                    b.explosion = True
                    # change le sprite de la balle quand le bonus est activé
                    b.load_sprite(C.TILESET_EXPL_POS, C.TILESET_BALLS_SIZE)
        # au bout d'un temps donné, les balles redeviennent normale
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            self.end = True
            for b in self.breakout.balls:
                if b.explosion:
                    b.explosion = False
                    # remet le sprite de la balle
                    b.load_sprite(C.TILESET_BALLS_POS, C.TILESET_BALLS_SIZE)
            self.use = False

    def unbreakable(self):
        """Malus qui rend une brique temporairement incassable"""

        # une brique est rendue incassable quand le malus est pris
        if not self.start:
            self.start = True
            # une brique aléatoire est rendue incassable
            self.unbrickable = rd.choice(self.breakout.brick_field.bricks)
            self.unbrickable.unbreakable = True

            # change le tileset, met l'image à la suite de la brique qui a le plus de vie
            pos = [
                C.TILESET_BRICKS_POS[0],
                C.TILESET_BRICKS_POS[1]
                + (C.TILESET_BRICKS_SIZE[1] + 1) * (C.BRICK_MAX_LIVES + 1),
            ]
            self.unbrickable.load_sprite(pos, C.TILESET_BRICKS_SIZE)

        # au bout d'un temps donné, la brique peut à nouveau être détruite
        elif (self.count > C.ACTIVATION_TIME) and not self.end:
            if self.unbrickable is not None:
                self.unbrickable.unbreakable = False
                # le tileset de la brique est rechargé
                pos = [
                    C.TILESET_BRICKS_POS[0],
                    C.TILESET_BRICKS_POS[1]
                    + (C.TILESET_BRICKS_SIZE[1] + 1) * (5 - (self.unbrickable.lives)),
                ]
                self.unbrickable.load_sprite(pos, C.TILESET_BRICKS_SIZE)
            self.end = True
            self.use = False


class Net(Game_object):
    """Permet d'afficher le filet"""

    def __init__(self, breakout, sprites):
        super().__init__(breakout, position=C.NET_POS, size=C.NET_SIZE, images=sprites)
        # charge l'image du filet
        self.load_sprite(C.TILESET_NET_POS, C.TILESET_NET_SIZE)

    def kill(self):
        """Destruction de l'objet"""

        # enlève l'image du filet
        self.breakout.all_sprites.remove(self)
        del self
