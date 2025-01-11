# name:     main.py
# author:
# date:     02.12.2024
#
# descrption: This file is ran by calling "python -m breakout". It runs the game

import pygame
import sys
import constants as C
from breakout import Breakout




# Initialize pygame
pygame.init()

# Initialize font
font = pygame.font.Font("breakout/fonts/bedstead.otf", C.TXT_FONT_SIZE)

# Set up the screen dimensions and create a window
screen_width, screen_height = C.WINDOW_WIDTH, C.WINDOW_HEIGHT
background_menu = pygame.image.load("breakout/tileset/backguound_Menu.png")
background_menu = pygame.transform.scale(background_menu, (screen_width, screen_height))

background_histoire = pygame.image.load("breakout/tileset/backguound_Histoire.png")
background_histoire = pygame.transform.scale(background_histoire, (screen_width, screen_height))

background_game = pygame.image.load("breakout/tileset/backguound_Game.png")
background_game = pygame.transform.scale(background_game, (screen_width, screen_height))


background_gameover = pygame.image.load("breakout/tileset/backguound_Gameover.png")
background_gameover = pygame.transform.scale(background_gameover, (screen_width, screen_height))

background_start= pygame.image.load("breakout/tileset/logo.png")
background_start = pygame.transform.scale(background_start, (screen_width, screen_height))


screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Fragments of Eternity")


# Définir l'icône de la fenêtre
pygame.display.set_icon(pygame.image.load('breakout/tileset/logo.png'))
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
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            waiting = False
    if pygame.time.get_ticks() - start_ticks > 4000:
        waiting = False

# Test d'ajout
while breakout.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            breakout.running = False

    if breakout.status == "menu":
        background_image = background_menu
        next_song = "breakout/son/menu.mp3"
    elif breakout.status == "playing":
        background_image = background_game
        next_song = "breakout/son/Whispers_of_Eternia.mp3"
    elif breakout.status == "game_over":
        background_image = background_gameover
    elif breakout.status == "histoire":
        background_image = background_histoire
        next_song = "breakout/son/Histoire.mp3"
       
         

    if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(next_song)
            pygame.mixer.music.play()

    # Draws background
    screen.blit(background_image, (0, 0))

    #screen.fill(C.WINDOW_BACKGROUND_COLOR)
    # Draws game
    breakout.show()
    # Update the display
    pygame.display.flip()

    if breakout.status == "game_over":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            # Reset the game
            del breakout
            # Create a Breakout object
            breakout = Breakout(screen, font)
    if  breakout.status == "histoire":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] or keys[pygame.K_SPACE] or keys[pygame.K_ESCAPE]:
            breakout.status = "menu"

    # Cap the frame rate to 60 frames per second
    clock.tick(60)


# Quit pygame
pygame.quit()
sys.exit()
