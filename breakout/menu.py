# name:     menu.py
# author:   Ding Jérémy
# date:     04.12.2024
#
import pygame


class Menu:
    def __init__(self, breakout, screen: pygame.display, font):
        # Game reference
        self.breakout = breakout
        self.screen = screen
        self.font = font

    def show(self):
        """Displays the menu"""
        # Check if the mouse is over the button
        s = self.screen
        # Get player mouse position
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Set default cursor
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        # Play button
        play_txt = self.font.render("Play", True, "Black")
        play_rec = play_txt.get_rect(center=(400, 200))

        # Quit button
        quit_txt = self.font.render("Quit", True, "Black")
        quit_rec = quit_txt.get_rect(center=(400, 400))

        # Check for mouse hover
        if play_rec.collidepoint(mouse_pos):  # Hover effect for "Play"
            play_bg_color = (100, 100, 100)
            play_txt_color = "Yellow"
            play_txt = self.font.render("Play", True, play_txt_color)
            pygame.draw.rect(self.screen, play_bg_color, play_rec.inflate(20, 10))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if quit_rec.collidepoint(mouse_pos):  # Hover effect for "Quit"
            quit_bg_color = (100, 100, 100)
            quit_txt_color = "Red"
            quit_txt = self.font.render("Quit", True, quit_txt_color)
            pygame.draw.rect(self.screen, quit_bg_color, quit_rec.inflate(20, 10))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Set cursor to hand

        # Check for a mouse press
        if play_rec.collidepoint(mouse_pos) and mouse_click[0]:
            self.breakout.status = "playing"
            
            # Set default cursor
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            # Jouer le fichier
            pygame.mixer.music.play()

        if quit_rec.collidepoint(mouse_pos) and mouse_click[0]:
            self.breakout.running = False

        s.blit(play_txt, play_rec)
        s.blit(quit_txt, quit_rec)
