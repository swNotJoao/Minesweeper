import pygame, time
from random import randint

# Grid
###############################################################################
class Grid:
    def __init__(self, width ,height, bombNumber, window):
        self.matrix = [[0 for i in range(width)] for j in range(height)]
        self.width = width
        self.height = height
        self.bombNumber = 0
        self.bombsLeft = width * height

        self.offsets = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1,1]]

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
                    print '[DEBUGGER] Mine placed in', x, y
                else:
                    self.matrix[x][y] = Tile(self.tileImg, x*40, y*40, False)

        for i in range(0, self.width):
            for j in range(0, self.height):
                counter = 0
                for coord in self.offsets:
                    x, y = coord[0], coord[1]
                    if (i+x >= 0) and (j+y >= 0) and (i+x < self.width) and (j+y < self.height):
                        if self.matrix[i+x][j+y].getIsMine():
                            counter = counter + 1
                self.matrix[i][j].bombNumber = counter


    def draw(self, window):
        for x in range (0, self.width):
            for y in range (0, self.height):
                self.matrix[x][y].draw(window)

    def click(self, i, j):
        print 'OPENING', i, j
        ret = self.matrix[i][j].open()

        if ret != -1:
            self.bombsLeft-=1
            print 'TILES LEFT', self.bombsLeft

            if ret == 0:
                for coord in self.offsets:
                    x, y = coord[0], coord[1]
                    if (i+x >= 0) and (j+y >= 0) and (i+x < self.width) and (j+y < self.height):
                        #self.matrix[i+x][j+y].open()
                        if self.matrix[i+x][j+y].state != 'opened':
                            self.click(i+x, j+y)
	    
        else:
	    aux = 0
	    for coord in self.offsets:
                    x, y = coord[0], coord[1]
                    if (i+x >= 0) and (j+y >= 0) and (i+x < self.width) and (j+y < self.height):
                        #self.matrix[i+x][j+y].open()
                        if self.matrix[i+x][j+y].getFlagState() == 'flagged':
                            aux +=1
	    #print aux
	    if aux == ret:
	        for coord in self.offsets:
                    x, y = coord[0], coord[1]
		    print "AQUI"
                    if (i+x >= 0) and (j+y >= 0) and (i+x < self.width) and (j+y < self.height):
                        #self.matrix[i+x][j+y].open()
                        if self.matrix[i+x][j+y].getFlagState() == 'closed':
                            self.click(i+x, j+y)
			    print "clicking " + str(i+x) +', ' + str(j+y)
            return -1

        if self.bombsLeft == self.bombNumber:
            print 'you won'

    def flag(self, i, j):
        self.matrix[i][j].flag()

# Tile
###############################################################################
class Tile:
    def __init__(self, img, x, y, isMine):
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
        self.flagImg = pygame.image.load('../assets/flag.png')
        self.flagImg = pygame.transform.scale(self.flagImg, (40, 40))
        self.questionMarkImg = pygame.image.load('../assets/?.png')
        self.questionMarkImg = pygame.transform.scale(self.questionMarkImg, (40, 40))
        self.bombImg = pygame.image.load('../assets/bomb.jpg')
        self.bombImg = pygame.transform.scale(self.bombImg, (40, 40))

        self.numbers = [self.mineImg0, self.mineImg1, self.mineImg2, self.mineImg3, self.mineImg4, self.mineImg5, self.mineImg6, self.mineImg7, self.mineImg8]

        self.img = img
        self.closedImg = img
        self.x = x
        self.y = y
        self.state = 'closed'
        self.isMine = isMine
        self.bombNumber = 0

    def draw(self, window):
        window.blit(self.img ,(self.x, self.y))

    def open(self):
        if self.state == 'closed':
            self.state = 'opened'

            if self.isMine:
                self.img = self.bombImg
            else:
                self.img = self.numbers[self.bombNumber]

            if self.isMine:
                return -1
            else:
                return self.bombNumber

    def flag(self):
        if self.state == 'closed':
            self.state = 'flagged'
            self.img = self.flagImg

        elif self.state == 'flagged':
            self.state = 'questionMark'
            self.img = self.questionMarkImg

        elif self.state == 'questionMark':
            self.state = 'closed'
            self.img = self.closedImg

    def setImg(self, img):
        self.img = img

    def getIsMine(self):
        return self.isMine

    def getFlagState(self):
	return self.state
