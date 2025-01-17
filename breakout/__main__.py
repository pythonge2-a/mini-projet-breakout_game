# name:     main.py
# author:
# date:     02.12.2024
#
# descrption: This file is ran by calling "python -m breakout". It runs the game

import pygame
import sys
import constants as C
from breakout import Breakout
import random


# Initialize pygame
pygame.init()

# Initialize font
font = pygame.font.Font("breakout/fonts/bedstead.otf", C.TXT_FONT_SIZE)

# Set up the screen dimensions and create a window
screen_width, screen_height = C.WINDOW_WIDTH, C.WINDOW_HEIGHT
background_menu = pygame.image.load("breakout/tileset/backguound_Menu.png")
background_menu = pygame.transform.scale(background_menu, (screen_width, screen_height))

background_histoire = pygame.image.load("breakout/tileset/backguound_Histoire.png")
background_histoire = pygame.transform.scale(
    background_histoire, (screen_width, screen_height)
)

backgrounds_levels = []
for i in range(C.LEVELS_NUMBER):
    background = pygame.image.load(f"breakout/tileset/backguound_level{i}.png")
    background = pygame.transform.scale(background, (screen_width, screen_height))
    backgrounds_levels.append(background)

background_gameover = pygame.image.load("breakout/tileset/backguound_Gameover.png")
background_gameover = pygame.transform.scale(
    background_gameover, (screen_width, screen_height)
)

background_start = pygame.image.load("breakout/tileset/logo.png")
background_start = pygame.transform.scale(
    background_start, (screen_width, screen_height)
)
background_win = pygame.image.load("breakout/tileset/backguound_Win.png")
background_win = pygame.transform.scale(background_win, (screen_width, screen_height))

background_win1 = pygame.image.load("breakout/tileset/backguound_Win1.png")
background_win1 = pygame.transform.scale(background_win1, (screen_width, screen_height))

background_win2 = pygame.image.load("breakout/tileset/backguound_Win2.png")
background_win2 = pygame.transform.scale(background_win2, (screen_width, screen_height))

background_win3 = pygame.image.load("breakout/tileset/backguound_Win3.png")
background_win3 = pygame.transform.scale(background_win3, (screen_width, screen_height))

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Fragments of Eternity")


# Définir l'icône de la fenêtre
pygame.display.set_icon(pygame.image.load("breakout/tileset/logo.png"))
# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Main loop
running = True

# Initialiser le mixer
pygame.mixer.init()
# Charger un fichier MP3
next_song = "breakout/son/menu.mp3"

pygame.mixer.music.load(next_song)
pygame.mixer.music.play()
# Create a Breakout object
breakout = Breakout(screen, font)

i = 0


# Draws background
screen.blit(background_start, (0, 0))

# Update the display
pygame.display.flip()

# Pause for 2 seconds or until a key is pressed
start_ticks = pygame.time.get_ticks()
waiting = True
progress = 0
loading_bar_length = 300
loading_bar_height = 30
loading_bar_x = (screen_width - loading_bar_length) // 2
loading_bar_y = screen_height - 50

while waiting:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            waiting = False

    # Loading bar animation
    screen.blit(background_start, (0, 0))
    pygame.draw.rect(
        screen,
        (140, 0, 140),
        (loading_bar_x, loading_bar_y, progress, loading_bar_height),
    )
    pygame.draw.rect(
        screen,
        (255, 255, 255),
        (loading_bar_x, loading_bar_y, loading_bar_length, loading_bar_height),
        2,
    )
    pygame.display.flip()

    progress += random.randint(0, 2)
    if progress > loading_bar_length:
        progress = loading_bar_length
        waiting = False

    pygame.time.delay(40)


def gest_song_bg():
    if breakout.status == "menu":
        background_image = background_menu
        next_song = "breakout/son/menu.mp3"
    elif breakout.status == "playing":
        if breakout.level == 0:
            next_song = "breakout/son/Whispers_of_Eternia.mp3"
        elif breakout.level == 1:
            if breakout.num_song == 0:
                next_song = "breakout/son/Les Lueurs du Mystère.mp3"
            else:
                next_song = "breakout/son/Les Lueurs du Mystère2.mp3"
        elif breakout.level == 2:
            if breakout.num_song == 0:
                next_song = "breakout/son/Les Murmures du Vide.mp3"
            else:
                next_song = "breakout/son/Les Questions Sans Réponses.mp3"
        elif breakout.level == 3:
            next_song = "breakout/son/Au Bout des Étoiles.mp3"
        elif breakout.level == 4:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Cœur Brisé des Mondes.mp3"
            else:
                next_song = "breakout/son/Le Cœur Brisé des Mondes2.mp3"
        elif breakout.level == 5:
            if breakout.num_song == 0:
                next_song = "breakout/son/Les Liens des Étoiles.mp3"
            else:
                next_song = "breakout/son/Les Liens des Étoiles2.mp3"
        elif breakout.level == 6:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Monde Caché.mp3"
            else:
                next_song = "breakout/son/Le Monde Caché2.mp3"
        elif breakout.level == 7:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Dernier Saut.mp3"
            else:
                next_song = "breakout/son/Le Dernier Saut2.mp3"
        elif breakout.level == 8:
            if breakout.num_song == 0:
                next_song = "breakout/son/Les Légions du Néant.mp3"
            else:
                next_song = "breakout/son/Les Légions du Néant2.mp3"
        elif breakout.level == 9:
            next_song = "breakout/son/Le_chant_du_Vide.mp3"
        elif breakout.level == 10:
            if breakout.num_song == 0:
                next_song = "breakout/son/L'Éclat des Survivants.mp3"
            else:
                next_song = "breakout/son/L'Éclat des Survivants2.mp3"
        elif breakout.level == 11:
            next_song = "breakout/son/L'Appel de Myrthos.mp3"
        elif breakout.level == 12:
            if breakout.num_song == 0:
                next_song = "breakout/son/L'Éveil des Failles.mp3"
            else:
                next_song = "breakout/son/L'Éveil des Failles2.mp3"
        elif breakout.level == 13:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Reflet d Ombros.mp3"
            else:
                next_song = "breakout/son/Le Reflet d Ombros2.mp3"
        elif breakout.level == 14:
            if breakout.num_song == 0:
                next_song = "breakout/son/La Chute des Gardiens.mp3"
            else:
                next_song = "breakout/son/La Chute des Gardiens2.mp3"
        elif breakout.level == 15:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Cœur Brisé.mp3"
            else:
                next_song = "breakout/son/Le Cœur Brisé2.mp3"
        elif breakout.level == 16:
            next_song = "breakout/son/Les Forges du Néant.mp3"
        elif breakout.level == 17:
            if breakout.num_song == 0:
                next_song = "breakout/son/Les Mondes Éclipsés.mp3"
            else:
                next_song = "breakout/son/Les Mondes Éclipsés2.mp3"
        elif breakout.level == 18:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Conclave des Gardiens.mp3"
            else:
                next_song = "breakout/son/Le Conclave des Gardiens2.mp3"
        elif breakout.level == 19:
            next_song = "breakout/son/L'Avatar du Vide.mp3"
        elif breakout.level == 20:
            next_song = "breakout/son/Le Sacrifice des Mondes.mp3"
        elif breakout.level == 21:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Jugement des Étoiles.mp3"
            else:
                next_song = "breakout/son/Le Jugement des Étoiles2.mp3"
        elif breakout.level == 22:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Dernier Éclat.mp3"
            else:
                next_song = "breakout/son/Le Dernier Éclat2.mp3"
        
        elif breakout.level == 23:
            if breakout.num_song == 0:
                next_song = "breakout/son/Les Ombres de Sol’Tarim.mp3"
            else:
                next_song = "breakout/son/Les Ombres de Sol’Tarim2.mp3"
        elif breakout.level == 24:
            if breakout.num_song == 0:
                next_song = "breakout/son/Les Échos de Mémoire.mp3"
            else:
                next_song = "breakout/son/Les Échos de Mémoire2.mp3"
        elif breakout.level == 25:
            next_song = "breakout/son/Le Rituel Interdit.mp3"
        elif breakout.level == 26:
            next_song = "breakout/son/L’Appel des Fragments.mp3"
        elif breakout.level == 27:
            next_song = "breakout/son/Au Cœur des Catacombes.mp3"
        elif breakout.level == 28:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Dilemme de l’Âme.mp3"
            else:
                next_song = "breakout/son/Le Dilemme de l’Âme2.mp3"
        elif breakout.level == 29:
            if breakout.num_song == 0:
                next_song = "breakout/son/L’Éveil du Gardien Réanimé.mp3"
            else:
                next_song = "breakout/son/L’Éveil du Gardien Réanimé2.mp3"
        elif breakout.level == 30:
            if breakout.num_song == 0:
                next_song = "breakout/son/La Confrontation.mp3"
            else:
                next_song = "breakout/son/La Confrontation2.mp3"
        elif breakout.level == 31:
            if breakout.num_song == 0:
                next_song = "breakout/son/Le Choix Décisif.mp3"
            else:
                next_song = "breakout/son/Le Choix Décisif2.mp3"
        elif breakout.level == 32:
            if breakout.num_song == 0:
                next_song = "breakout/son/L’Aube d’un Nouveau Cycle.mp3"
            else:
                next_song = "breakout/son/L’Aube d’un Nouveau Cycle2.mp3"
        background_image = backgrounds_levels[breakout.level]
    elif breakout.status == "game_over":
        background_image = background_gameover
        next_song = "breakout/son/game_over.mp3"
    elif breakout.status == "histoire" or breakout.status == "histoire_summary":
        background_image = background_histoire
        next_song = "breakout/son/Histoire.mp3"
    elif breakout.status == "win":
        background_image = background_win
        next_song = "breakout/son/Fragments d’Éternité.mp3"
    elif breakout.status == "win1":
        background_image = background_win1
        next_song = "breakout/son/Lumière Éternelle.mp3"
    elif breakout.status == "win2":
        background_image = background_win2
        next_song = "breakout/son/Le Cycle Éternel.mp3"
    elif breakout.status == "win3":
        background_image = background_win3
        next_song = "breakout/son/L'Étoile Qui S'Éteint.mp3"
    if not pygame.mixer.music.get_busy():
        if breakout.num_song == 0:
            breakout.num_song = 1
        else:
            breakout.num_song = 0
        pygame.mixer.music.load(next_song)
        pygame.mixer.music.play()
        # Draws background
    screen.blit(background_image, (0, 0))


# Test d'ajout
while breakout.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            breakout.running = False

    gest_song_bg()

    # Draws game
    breakout.show()
    # Update the display
    pygame.display.flip()

    if (
        breakout.status == "game_over"
        or breakout.status == "win1"
        or breakout.status == "win2"
        or breakout.status == "win3"
        or breakout.status == "win"
    ):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            # Reset the game
            del breakout
            # Create a Breakout object
            breakout = Breakout(screen, font)

    if breakout.status == "histoire" or breakout.status == "histoire_summary":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            breakout.status = "menu"

    # Cap the frame rate to 60 frames per second
    clock.tick(60)


# Quit pygame
pygame.quit()
sys.exit()
