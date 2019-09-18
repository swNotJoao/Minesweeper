import pygame, sys, os
from tile import Tile
from grid import Grid

#Globals
_windowWidth = 400
_windowHeight = 400
_gridWidth = 10
_gridHeight = 10
_cellWidth = _windowWidth / _gridWidth
_cellHeight = _windowHeight / _gridHeight
_bombNumber = 10

# Setup
pygame.init()
pygame.display.set_caption('Minesweeper v1.0b')
screen = pygame.display.set_mode((_windowWidth, _windowHeight))
programRunning = True

grid = Grid(_gridWidth, _gridHeight, 20, screen)

# Main loop
while programRunning:

    #Draw frame!
    grid.draw(screen)

    #Check for quit event caused by user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programFinished = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            squarex, squarey = x // _cellWidth, y // _cellHeight
            #Check for left mouse button press
            if event.button == 1:
                print "[!] Touched", x, y, squarex, squarey
                grid.click(squarex, squarey)
            #Check for right mouse button press
            elif event.button == 3:
                print "[!] Flagged", x, y, squarex, squarey

    pygame.display.flip()
