import pygame


class Racket:
    def __init__(self, screen, x, y, width = 5, height = 20, color =  (255, 255, 255) ,speed = 10):

        self.screen = screen
        if x == None:
            self.x = (screen.get_width() - width) // 2
        else:
            self.x = x
        if y == None:
            self.y = screen.get_height() / 20 + height
        else:
            self.y = y

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def move(self):
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x < self.screen.get_width() - self.width:
            self.x += self.speed    

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_speed(self):
        return self.speed
    
    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_width(self, width):
        self.width = width  

    def set_height(self, height):
        self.height = height            

    def set_speed(self, speed):
        self.speed = speed

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
