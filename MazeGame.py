import os
import sys
import random
import pygame
import os
from PyQt5.QtWidgets import (
QApplication, QWidget,
QFileDialog,
QLabel, QPushButton, QListWidget,
QHBoxLayout, QVBoxLayout
)


 
# Class for the orange dude
class Player(object):
    
    def __init__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)
 
    def move(self, dx, dy):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    
    def move_single_axis(self, dx, dy):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
 
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom

 
def playmusic():
    pygame.mixer.init()
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play()
playmusic()
# Nice class to hold a wall rect
class Wall(object):
    
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
    
 
# Initialise pygame
os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
 
# Set up the display
pygame.display.set_caption("Maze Project.")
screen = pygame.display.set_mode((768, 240))
 
clock = pygame.time.Clock()
walls = [] # List to hold the walls
player = Player() # Create the player
secrets = []
 
# Holds the level layout in a list of strings.
level = [
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
    "W         WWW   WWW  WWWWW    W        WWW   E W",
    "W         WWWWWW  WWW         WWW              W",
    "W   WWWW       W    Y  WWW      W   WW      W  W",
    "W   W        WWWW W WWW  W   WWWW           W  W",
    "W WWW  WWWW     WWW    WWW    RWWWWW     WWWW  W",
    "W   W     W W     W    W  WWWW      W      WW WW",
    "W   W     W   WWWWW WWWW        WWWW    WWW    W",
    "W   WWW WWW   W W   W WWWWW W   W     WWWWWWWW W",
    "W     W   W   W W   W W     W   WWWWWW         W",
    "WWW   W   WWWWW W  WW W     W        WWWWTWWWWWW",
    "W W      WW           WWW   W WWW    W         W",
    "W W   WWWW   WWWWWWWWWW       W     WWWWWW     W",
    "W     U    W   W      W     WWW                W",
    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
 
# Parse the level string above. W = wall, E = exit R = Secret wall
x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        if col == "R":
            secret = pygame.Rect(x, y, 16, 16)
        if col == "T":
            secret2 = pygame.Rect(x, y, 16, 16)
        if col == "Y":
            secret3 = pygame.Rect(x, y, 16, 16)
        if col == "U":
            secret4 = pygame.Rect(x, y, 16, 16)
            
        x += 16
    y += 16
    x = 0
 
running = True

while running:
    
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False
 
    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player.move(-2, 0)
    if key[pygame.K_RIGHT]:
        player.move(2, 0)
    if key[pygame.K_UP]:
        player.move(0, -2)
    if key[pygame.K_DOWN]:
        player.move(0, 2)
 
    # Just added this to make it slightly fun ;)
    if player.rect.colliderect(end_rect):
        print("You finished! You can sit back and enjoy the music :)")
        end_rect = pygame.Rect(x, y, 18, 18)

    if player.rect.colliderect(secret):
        secret = pygame.Rect(x, y, 18, 18)
    
    if player.rect.colliderect(secret2):
        secret2 = pygame.Rect(x, y, 18, 18)

    if player.rect.colliderect(secret3):
        secret3 = pygame.Rect(x, y, 18, 18)
    
    if player.rect.colliderect(secret4):
        secret4 = pygame.Rect(x, y, 18, 18)
 
    # Draw the scene
    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, (255, 200, 0), player.rect)
    pygame.draw.rect(screen, (255, 255, 255), secret)
    pygame.draw.rect(screen, (255, 255, 255), secret2)
    pygame.draw.rect(screen, (255, 255, 255), secret3)
    pygame.draw.rect(screen, (255, 255, 255), secret4)
    # gfxdraw.filled_circle(screen, 255, 200, 5, (0,128,0))
    pygame.display.flip()
    clock.tick(360)
 
pygame.quit()
