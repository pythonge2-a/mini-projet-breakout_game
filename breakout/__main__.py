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

background_win = pygame.image.load("breakout/tileset/backguound_win.png")
background_win = pygame.transform.scale(background_win, (screen_width, screen_height))

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
            if random.randint(0, 1) == 0:
                next_song = "breakout/son/Les Lueurs du Mystère.mp3"
            else:
                next_song = "breakout/son/Les Lueurs du Mystère2.mp3"
        elif breakout.level == 2:
            next_song = "breakout/son/Les Murmures du vide .mp3"
        elif breakout.level == 3:
            next_song = "breakout/son/Au Bout des Étoiles.mp3"
        elif breakout.level == 4:
            if random.randint(0, 1) == 0:
                next_song = "breakout/son/Le Cœur Brisé des Mondes.mp3"
            else:
                next_song = "breakout/son/Le Cœur Brisé des Mondes2.mp3"
        elif breakout.level == 5:
            if random.randint(0, 1) == 0:
                next_song = "breakout/son/Les Liens des Étoiles.mp3"
            else:
                next_song = "breakout/son/Les Liens des Étoiles2.mp3"
        elif breakout.level == 6:
            if random.randint(0, 1) == 0:
                next_song = "breakout/son/Le Monde Caché.mp3"
            else:
                next_song = "breakout/son/Le Monde Caché2.mp3"
        elif breakout.level == 7:
            if random.randint(0, 1) == 0:
                next_song = "breakout/son/Le Dernier Saut.mp3"
            else:
                next_song = "breakout/son/Le Dernier Saut2.mp3"
        elif breakout.level == 8:
            if random.randint(0, 1) == 0:
                next_song = "breakout/son/Les Légions du Néant.mp3"
            else:
                next_song = "breakout/son/Les Légions du Néant2.mp3"
        elif breakout.level == 9:
            next_song = "breakout/son/Le_chant_du_Vide.mp3"
        elif breakout.level == 10:
            if random.randint(0, 1) == 0:
                next_song = "breakout/son/L'Éclat des Survivants.mp3"
            else:
                next_song = "breakout/son/L'Éclat des Survivants2.mp3"

        background_image = backgrounds_levels[breakout.level]
    elif breakout.status == "game_over":
        background_image = background_gameover
        next_song = "breakout/son/game_over.mp3"
    elif breakout.status == "histoire" or breakout.status == "histoire_summary":
        background_image = background_histoire
        next_song = "breakout/son/Histoire.mp3"
    elif breakout.status == "win":
        background_image = background_win
        next_song = "breakout/son/Lumière Éternelle.mp3"

    if not pygame.mixer.music.get_busy():
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

    if breakout.status == "game_over" or breakout.status == "win":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            # Reset the game
            del breakout
            # Create a Breakout object
            breakout = Breakout(screen, font)

    if breakout.status == "histoire":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            breakout.status = "menu"

    # Cap the frame rate to 60 frames per second
    clock.tick(60)


# Quit pygame
pygame.quit()
sys.exit()
