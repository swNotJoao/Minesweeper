from tile import Tile

class Grid:
    def __init__(self, width ,height, bombNumber):
        self.matrix = [[]]
        self.bombNumber = bombNumber

        self.mineImg0 = pygame.image.load('../assets/0.png')
        self.mineImg0 = pygame.transform.scale(mineImg0, (40, 40))
        self.mineImg1 = pygame.image.load('../assets/1.png')
        self.mineImg1 = pygame.transform.scale(mineImg1, (40, 40))
        self.mineImg2 = pygame.image.load('../assets/2.png')
        self.mineImg2 = pygame.transform.scale(mineImg2, (40, 40))
        self.mineImg3 = pygame.image.load('../assets/3.png')
        self.mineImg3 = pygame.transform.scale(mineImg3, (40, 40))
        self.mineImg4 = pygame.image.load('../assets/4.png')
        self.mineImg4 = pygame.transform.scale(mineImg4, (40, 40))
        self.mineImg5 = pygame.image.load('../assets/5.png')
        self.mineImg5 = pygame.transform.scale(mineImg5, (40, 40))
        self.mineImg6 = pygame.image.load('../assets/6.png')
        self.mineImg6 = pygame.transform.scale(mineImg6, (40, 40))
        self.mineImg7 = pygame.image.load('../assets/7.png')
        self.mineImg7 = pygame.transform.scale(mineImg7, (40, 40))
        self.mineImg8 = pygame.image.load('../assets/8.png')
        self.mineImg8 = pygame.transform.scale(mineImg8, (40, 40))

    def init(self):
        for x in range (0, 9):
            for y in range (0, 9):
                self.matrix[x][y] = Tile()
