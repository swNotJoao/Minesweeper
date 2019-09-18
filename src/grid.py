from tile import Tile
import pygame
from random import randint

class Grid:
    def __init__(self, width ,height, bombNumber, window):
        self.matrix = [[0 for i in range(10)] for j in range(10)]
        self.width = width
        self.height = height
        self.bombNumber = 0

        self.mineImg0 = pygame.image.load('../assets/0.png')
        self.mineImg0 = pygame.transform.scale(self.mineImg0, (40, 40))
        self.mineImg1 = pygame.image.load('../assets/1.png')
        self.mineImg1 = pygame.transform.scale(self.mineImg1, (40, 40))
        self.mineImg2 = pygame.image.load('../assets/2.png')
        self.mineImg2 = pygame.transform.scale(self.mineImg2, (40, 40))
        self.mineImg3 = pygame.image.load('../assets/3.png')
        self.mineImg3 = pygame.transform.scale(self.mineImg3, (40, 40))
        self.mineImg4 = pygame.image.load('../assets/4.png')
        self.mineImg4 = pygame.transform.scale(self.mineImg4, (40, 40))
        self.mineImg5 = pygame.image.load('../assets/5.png')
        self.mineImg5 = pygame.transform.scale(self.mineImg5, (40, 40))
        self.mineImg6 = pygame.image.load('../assets/6.png')
        self.mineImg6 = pygame.transform.scale(self.mineImg6, (40, 40))
        self.mineImg7 = pygame.image.load('../assets/7.png')
        self.mineImg7 = pygame.transform.scale(self.mineImg7, (40, 40))
        self.mineImg8 = pygame.image.load('../assets/8.png')
        self.mineImg8 = pygame.transform.scale(self.mineImg8, (40, 40))
        self.questionMarkImg = pygame.image.load('../assets/?.png')
        self.questionMarkImg = pygame.transform.scale(self.questionMarkImg, (40, 40))
        self.flagImg = pygame.image.load('../assets/flag.png')
        self.flagImg = pygame.transform.scale(self.flagImg, (40, 40))
        self.tileImg = pygame.image.load('../assets/tile.png')
        self.tileImg = pygame.transform.scale(self.tileImg, (40, 40))
        self.bombImg = pygame.image.load('../assets/bomb.jpg')
        self.bombImg = pygame.transform.scale(self.bombImg, (40, 40))

        for x in range (0, self.width):
            for y in range (0, self.height):
                if (self.bombNumber < bombNumber) and (randint(0, 5) == 1):
                    self.matrix[x][y] = Tile(self.tileImg, x*40, y*40, True)
                    self.bombNumber += 1
                else:
                    self.matrix[x][y] = Tile(self.tileImg, x*40, y*40, False)

    def draw(self, window):
        for x in range (0, self.width):
            for y in range (0, self.height):
                self.matrix[x][y].draw(window)

    def click(self, i, j):
        self.matrix[i][j].open()
        if self.matrix[i][j].getIsMine():
            self.matrix[i][j].setImg(self.bombImg)
        else:
            self.matrix[i][j].setImg(self.mineImg0)
