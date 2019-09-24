class Tile:

    def __init__(self, img, x, y, isMine):
        self.img = img
        self.x = x
        self.y = y
        self.state = 'closed'
        self.isMine = isMine

    def draw(self, window):
        window.blit(self.img ,(self.x, self.y))

    def open(self):
        self.state = 'opened'
        if self.isMine:
            print "GAME OVER"

    def setImg(self, img):
        self.img = img

    def getIsMine(self):
        return self.isMine
