# Importing modules
import pygame as P_Game
import numpy as np
import os
import grid

# Environment configuration
os.environ["SDL_VIDEO_CENTERED"] = '1'

# resolution
width, height = 1920, 1080
size = (width, height)


P_Game.init()
P_Game.display.set_caption("CONWAY'S GAME OF LIFE")
screen = P_Game.display.set_mode(size)
clock = P_Game.time.Clock()
fps = 20

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0, 14, 71)
white = (255, 255, 255)

scaler = 30
offset = 1

Grid = grid.Grid(width, height, scaler, offset)
Grid.random2d_array()


pause = False
run = True

while run:
    clock.tick(fps)
    screen.fill(black)

    # Commands
    for event in P_Game.event.get():
        if event.type == P_Game.QUIT:
            run = False
        if event.type == P_Game.KEYUP:
            if event.key == P_Game.K_ESCAPE:
                run = False
            if event.key == P_Game.K_SPACE:
                pause = not pause

    Grid.Conway(off_color=white, on_color=blue1, surface=screen, pause=pause)

    if P_Game.mouse.get_pressed()[0]:
        mouseX, mouseY = P_Game.mouse.get_pos()
        Grid.HandleMouse(mouseX, mouseY)

    P_Game.display.update()

P_Game.quit()

'''
Created By Shourya Gupta
'''
