import pygame, sys, os
from tile import Tile

# Setup
pygame.init()
pygame.display.set_caption('Minesweeper v1.0b')
screen = pygame.display.set_mode((400, 400))
programRunning = True

mineImg0 = pygame.image.load('../assets/0.png')
mineImg0 = pygame.transform.scale(mineImg0, (40, 40))
mineImg1 = pygame.image.load('../assets/1.png')
mineImg1 = pygame.transform.scale(mineImg1, (40, 40))
mineImg2 = pygame.image.load('../assets/2.png')
mineImg2 = pygame.transform.scale(mineImg2, (40, 40))
mineImg3 = pygame.image.load('../assets/3.png')
mineImg3 = pygame.transform.scale(mineImg3, (40, 40))
mineImg4 = pygame.image.load('../assets/4.png')
mineImg4 = pygame.transform.scale(mineImg4, (40, 40))
mineImg5 = pygame.image.load('../assets/5.png')
mineImg5 = pygame.transform.scale(mineImg5, (40, 40))
mineImg6 = pygame.image.load('../assets/6.png')
mineImg6 = pygame.transform.scale(mineImg6, (40, 40))
mineImg7 = pygame.image.load('../assets/7.png')
mineImg7 = pygame.transform.scale(mineImg7, (40, 40))
mineImg8 = pygame.image.load('../assets/8.png')
mineImg8 = pygame.transform.scale(mineImg8, (40, 40))

tile1 = Tile(mineImg0, 0,0, False)
tile2 = Tile(mineImg1, 43,0, False)

# Main loop
while programRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            programFinished = True
            pygame.quit()
            sys.exit()

    tile1.draw(screen)
    tile2.draw(screen)
    pygame.display.flip()
