"""Our Hack110 project! (Subject tbd)"""

'''
# Imports
import pygame
# import pygame_gui
import sys
import random
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Set buttons objects
objects = []

pygame.mixer.init()

# ---------- Variables ------------------------------
# Initiate pygame
pygame.init()
fps = 60

# initiate pygame_gui manager and clock
manager = pygame_gui.UIManager((1280, 720))
clock = pygame.time.Clock()

# Background music
pygame.mixer.music.load("John Deere.mp3")
pygame.mixer.music.play(loops=-1)

# Screen size - Making the Background
screen = pygame.display.set_mode([1280, 720])
pygame.display.set_caption("John Deere's Great Pumpkin Harvest")
dt = 0


# -------- Game Start ---------------------------------------------------------------------------------------------
# Begin running the game!
running = True
while running:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        # Stops running if user closes window
        if event.type == QUIT:
            running = False
        # Stops running if user clicks escape key
        elif event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False
        manager.process_events(event)
    manager.update(time_delta)    
    
    # --- Update UI -----------
    screen.fill((52, 119, 42))

        # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(fps) / 1000

pygame.quit()

print("works")
'''

import pygame 
  
pygame.init() 
  
color = (255,255,255) 
rect_color = (255,0,0) 
  
# CREATING CANVAS 
canvas = pygame.display.set_mode((500,500)) 
  
# TITLE OF CANVAS 
pygame.display.set_caption("Show Image") 
  
image = pygame.image.load("Screenshot.png") 
exit = False
  
while not exit: 
    canvas.fill(color) 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit = True
  
    pygame.draw.rect(canvas, rect_color, 
                     pygame.Rect(30,30,60,60)) 
    pygame.display.update() 
