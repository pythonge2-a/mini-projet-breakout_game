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

        self.Son_brique = pygame.mixer.Sound("breakout/son/Brique.wav")
        self.Son_rackette = pygame.mixer.Sound("breakout/son/Raquette.wav")
        self.Son_bonus = pygame.mixer.Sound("breakout/son/Bonus.wav")

        # Define screen object
        self.screen = screen

        # Text font
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

        # Defines animation array (for particles)
        self.Animation_Break = []

        # Add bricks to sprites list
        for b in self.brick_field.bricks:
            self.all_sprites.add(b)
        # Add ball to sprites list
        self.all_sprites.add(self.balls[0])

        # Add racket
        self.all_sprites.add(self.racket)

        self.font_bold = pygame.font.SysFont("Arial", self.font.get_height(), bold=True)
        # On charge et on « wrap » l’histoire
        self.histoire_lines = self.load_histoire("breakout/histoire.txt")
        self.histoire_offset = C.WINDOW_HEIGHT

    def update(self):
        """Run a \"Game tick\" Update object's position, read player input etc."""
        # If no more balls are at play
        if self.balls == []:
            self.status = "game_over"
        else:
            for b in self.balls:
                b.update()

        # Move the racket according to player inputs
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

        if not self.Animation_Break:
            # Dessiner les animations en cours
            for anim in self.Animation_Break:
                anim.draw(self.screen)

        self.all_sprites.draw(self.screen)

    def show_menu(self):
        """Displays the game menu"""
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
        elif self.status == "histoire":
            self.show_histoire()

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

    def load_histoire(self, filepath):
        """
        Lit le fichier et renvoie une liste de lignes,
        où chaque ligne est une liste de tokens (mot, booléen_de_gras).
        """
        with open(filepath, "r", encoding="utf-8") as f:
            raw_text = f.read()

        # On découpe le texte en paragraphes (séparés par \n)
        paragraphs = raw_text.split("\n")

        # On va stocker toutes les lignes finalisées dans "all_lines"
        # Chaque "ligne" sera un tableau de tokens : [(word, is_bold), ...]
        all_lines = []

        max_width = int(C.WINDOW_WIDTH * 0.8)  # Par ex. 80% de la largeur de la fenêtre

        # Pour chaque paragraphe
        for paragraph in paragraphs:
            # Si le paragraphe est vide -> ligne vide forcée
            if not paragraph.strip():
                all_lines.append([])  # liste vide = ligne vide
                continue

            # 1) Découper les zones en gras via '**'
            tokens = []  # liste de (mot, is_bold)
            split_bold = paragraph.split("**")

            # Par alternance : si i est impair => on est dans une zone en gras
            is_bold = False
            for i, chunk in enumerate(split_bold):
                # i impair => ce chunk est en gras
                if i % 2 == 1:
                    is_bold = True
                else:
                    is_bold = False

                # On découpe ce morceau en "mots"
                words = chunk.split()
                for w in words:
                    tokens.append((w, is_bold))

            # 2) Word wrap : convertir "tokens" en "lignes" en tenant compte de max_width
            current_line_tokens = []
            current_line_width = 0
            first_token_in_line = True

            for word, bold in tokens:
                # Mesure du mot selon qu'il est bold ou non
                if bold:
                    w_width, _ = self.font_bold.size(word)
                else:
                    w_width, _ = self.font.size(word)

                # Largeur de l'espace avant le mot (sauf si c'est le 1er de la ligne)
                space_width, _ = self.font.size(" ")
                add_width = w_width + (0 if first_token_in_line else space_width)

                if current_line_width + add_width <= max_width:
                    # Ça rentre dans la ligne
                    current_line_tokens.append((word, bold))
                    current_line_width += add_width
                    first_token_in_line = False
                else:
                    # On doit passer à la ligne suivante
                    all_lines.append(current_line_tokens)
                    # On redémarre une nouvelle ligne
                    current_line_tokens = [(word, bold)]
                    current_line_width = w_width
                    first_token_in_line = False

            # Fin du paragraphe : on ajoute la dernière ligne si elle n'est pas vide
            if current_line_tokens:
                all_lines.append(current_line_tokens)

        return all_lines
        
    def show_histoire(self):

        y = self.histoire_offset
        
        # Parcourt chaque ligne (liste de tokens)
        for line_tokens in self.histoire_lines:
            # 1) Calcul de la hauteur de la ligne et de sa largeur totale
            line_height = 0
            total_line_width = 0
            
            # On va prévoir un espace (en pixels) entre chaque mot
            space_width, _ = self.font.size(" ")
            
            # Pour savoir si on est sur le premier token (pour ne pas ajouter d'espace avant)
            first_token = True
            
            for (word, is_bold) in line_tokens:
                # Choisir la police
                if is_bold:
                    font_used = self.font_bold
                else:
                    font_used = self.font
                
                word_w, word_h = font_used.size(word)
                
                # Mise à jour de la hauteur max de la ligne
                if word_h > line_height:
                    line_height = word_h
                
                # Mise à jour de la largeur totale
                #  - on ajoute un espace sauf pour le premier mot
                if first_token:
                    total_line_width += word_w
                    first_token = False
                else:
                    total_line_width += (space_width + word_w)
            
            # 2) Calcul de la position X pour centrer la ligne
            x = (C.WINDOW_WIDTH - total_line_width) // 2
            
            # 3) Affichage effectif de la ligne
            first_token = True
            for (word, is_bold) in line_tokens:
                if is_bold:
                    font_used = self.font_bold
                    color_texte = (255, 255, 30)
                else:
                    font_used = self.font
                    color_texte = (255, 255, 0)
                # Espace avant le mot (sauf pour le premier)
                if not first_token:
                    self.screen.blit(font_used.render(" ", True, color_texte), (x, y))
                    x += space_width
                else:
                    first_token = False
                
                # Dessin du mot
                word_surface = font_used.render(word, True, color_texte)
                self.screen.blit(word_surface, (x, y))
                x += word_surface.get_width()
            
            # Nouvelle ligne (on descend de line_height + 5)
            y += (line_height + 5)
        
        # Défilement vers le haut
        self.histoire_offset -= 1

        # Si tout est sorti de l'écran, on revient au menu
        if y < 0:
            self.histoire_offset = C.WINDOW_HEIGHT
            self.status = "menu"
