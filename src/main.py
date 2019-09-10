import pygame, sys, os
from tile import Tile

# Setup
pygame.init()
pygame.display.set_caption('Minesweeper v1.0b')
screen = pygame.display.set_mode((400, 400))
programRunning = True

# Main loop
while programRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programFinished = True
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            squarex, squarey = x//40, y//40
            if event.button == 1:
                print "[!] Touched", x, y, squarex, squarey
            elif event.button == 3:
                print "[!] Flagged", x, y, squarex, squarey

    pygame.display.flip()
