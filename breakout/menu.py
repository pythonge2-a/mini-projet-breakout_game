# name:     menu.py
# author:   Ding Jérémy
# date:     04.12.2024
#
import pygame
import constants as C
import os

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
        play_txt = self.font.render("New Adventure", True, "white")
        play_rec = play_txt.get_rect(center=(400, 100))

        # Quit button
        quit_txt = self.font.render("Quit", True, "white")
        quit_rec = quit_txt.get_rect(center=(400, 500))

        # History button
        histoire_txt = self.font.render("History", True, "white")
        histoire_rec = histoire_txt.get_rect(center=(400, 300))

        # History Summary button
        histoire_summary_txt = self.font.render("History Summary", True, "white")
        histoire_summary_rec = histoire_summary_txt.get_rect(center=(400, 400))

        # Continue button
        continue_txt = self.font.render("Continue", True, "white")
        continue_rec = continue_txt.get_rect(center=(400, 200))

        # Check for mouse hover
        if play_rec.collidepoint(mouse_pos):  # Hover effect for "Play"
            play_bg_color = (100, 100, 100)
            play_txt_color = "Yellow"
            play_txt = self.font.render("New Adventure", True, play_txt_color)
            pygame.draw.rect(self.screen, play_bg_color, play_rec.inflate(20, 10))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        if quit_rec.collidepoint(mouse_pos):  # Hover effect for "Quit"
            quit_bg_color = (100, 100, 100)
            quit_txt_color = "Red"
            quit_txt = self.font.render("Quit", True, quit_txt_color)
            pygame.draw.rect(self.screen, quit_bg_color, quit_rec.inflate(20, 10))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Set cursor to hand

        if histoire_rec.collidepoint(mouse_pos):  # Hover effect for "History"
            histoire_bg_color = (100, 100, 100)
            histoire_txt_color = "Blue"
            histoire_txt = self.font.render("History", True, histoire_txt_color)
            pygame.draw.rect(self.screen, histoire_bg_color, histoire_rec.inflate(20, 10))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Set cursor to hand

        if histoire_summary_rec.collidepoint(mouse_pos):  # Hover effect for "History Summary"
            histoire_summary_bg_color = (100, 100, 100)
            histoire_summary_txt_color = "Green"
            histoire_summary_txt = self.font.render("History Summary", True, histoire_summary_txt_color)
            pygame.draw.rect(self.screen, histoire_summary_bg_color, histoire_summary_rec.inflate(20, 10))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Set cursor to hand

        if continue_rec.collidepoint(mouse_pos):  # Hover effect for "Continue"
            continue_bg_color = (100, 100, 100)
            continue_txt_color = "Orange"
            continue_txt = self.font.render("Continue", True, continue_txt_color)
            pygame.draw.rect(self.screen, continue_bg_color, continue_rec.inflate(20, 10))
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # Set cursor to hand

        # Check for a mouse press
        if play_rec.collidepoint(mouse_pos) and mouse_click[0]:
            self.breakout.status = "playing"
            # Set default cursor
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            # Load and play a music file
            pygame.mixer.music.load("breakout/son/Whispers_of_Eternia.mp3")
            pygame.mixer.music.play()

        if quit_rec.collidepoint(mouse_pos) and mouse_click[0]:
            self.breakout.running = False

        if histoire_rec.collidepoint(mouse_pos) and mouse_click[0]:
            self.breakout.status = "histoire"
            # Set default cursor
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.breakout.histoire_offset = C.WINDOW_HEIGHT
            # Load and play a music file
            pygame.mixer.music.load("breakout/son/Histoire.mp3")
            pygame.mixer.music.play()

        if histoire_summary_rec.collidepoint(mouse_pos) and mouse_click[0]:
            self.breakout.status = "histoire_summary"
            # Set default cursor
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.breakout.histoire_offset = C.WINDOW_HEIGHT

            # Load and play a music file
            pygame.mixer.music.load("breakout/son/Histoire_speed.mp3")
            pygame.mixer.music.play()

        if continue_rec.collidepoint(mouse_pos) and mouse_click[0]:
            self.breakout.status = "playing"
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if os.path.exists("breakout/save.txt"):
                with open("breakout/save.txt", "r", encoding="utf-8") as f:
                    Save_Texte = f.read()
                    Save_Texte = Save_Texte.split("\n")
                    if len(Save_Texte) > 1:
                        if int(Save_Texte[0]) < C.LEVELS_NUMBER:
                            self.breakout.level = int(Save_Texte[0])
                            self.breakout.score = int(Save_Texte[1])
                            self.breakout.init = True
               

            
        s.blit(play_txt, play_rec)
        s.blit(quit_txt, quit_rec)
        s.blit(histoire_txt, histoire_rec)
        s.blit(histoire_summary_txt, histoire_summary_rec)
        s.blit(continue_txt, continue_rec)
