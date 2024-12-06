# name:     menu.py
# author:   Ding Jérémy
# date:     04.12.2024
#
import pygame


class Menu:
    def __init__(self, screen: pygame.display, font):
        self.screen = screen
        self.font = font

    def show(self):
        """Displays the menu"""
        # Check if the mouse is over the button
        s = self.screen
        # Get player mouse position
        mouse_pos = pygame.mouse.get_pos()

        play_txt = self.font.render("Play", True, "White")
        play_rec = play_txt.get_rect(center=(400, 200))

        quit_txt = self.font.render("Quit", True, "White")
        quit_rec = quit_txt.get_rect(center=(400, 400))
        s.blit(play_txt, play_rec)
        s.blit(quit_txt, quit_rec)
