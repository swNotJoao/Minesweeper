import pygame, sys, os, time
from Objects import Grid, Tile

#Globals
_windowWidth = 400
_windowHeight = 400
_gridWidth = 10
_gridHeight = 10
_cellWidth = _windowWidth / _gridWidth
_cellHeight = _windowHeight / _gridHeight
_bombNumber = 15

# Setup
pygame.init()
pygame.display.set_caption('Minesweeper v1.0b')
os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((_windowWidth, _windowHeight))
programRunning = True
gameOver = False

grid = Grid(_gridWidth, _gridHeight, _bombNumber, screen)

# Main loop
while programRunning:
    if gameOver:
        programRunning = False
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
                ret = grid.click(squarex, squarey)

                if ret == 1:
                    print 'YOU WON'
                    gameOver = True
                elif ret == -1:
                    print 'GAME OVER'
                    gameOver = True
            #Check for right mouse button press
            elif event.button == 3:
                grid.flag(squarex, squarey)

    pygame.display.flip()
