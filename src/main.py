import pygame, sys, os
from tile import Tile
from grid import Grid

# Setup
pygame.init()
pygame.display.set_caption('Minesweeper v1.0b')
screen = pygame.display.set_mode((400, 400))
programRunning = True

grid = Grid(10, 10, 0, screen)

# Main loop
while programRunning:
    #Check for quit event caused by user
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programFinished = True
            pygame.quit()
            sys.exit()

        #Draw frame!

        grid.draw()

        if event.type == pygame.MOUSEBUTTONUP:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            squarex, squarey = x//40, y//40
            #Check for left mouse button press
            if event.button == 1:
                print "[!] Touched", x, y, squarex, squarey
            #Check for right mouse button press
            elif event.button == 3:
                print "[!] Flagged", x, y, squarex, squarey

    pygame.display.flip()
