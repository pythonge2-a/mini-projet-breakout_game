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

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout Game")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()

# Main loop
running = True

# Create a Breakout object
breakout = Breakout(screen, font)

print(C.BRICK_WIDTH, C.BRICK_HEIGHT)

# Test d'ajout
while breakout.running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            breakout.running = False
    # Draws background
    screen.fill(C.WINDOW_BACKGROUND_COLOR)
    # Draws game
    breakout.show()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
