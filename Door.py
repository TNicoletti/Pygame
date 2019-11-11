from platform import *
class Door(Platform):

    def __init__(self,  x, y, width, height, ori):
        self.iX = x
        self.iY = y

        self.ori = ori

        super().__init__(x, y, width, height)

    def move(self):
        vel = 1

        walkHowMuch = 250

        if(self.ori == "right"):
            if(self.x <= self.iX + walkHowMuch ):
                self.x += vel
        if (self.ori == "left"):
            if (self.x >= self.iX - walkHowMuch):
                self.x -= vel
        if (self.ori == "down"):
            if (self.y <= self.iY + walkHowMuch):
                self.y += vel
        if (self.ori == "up"):
            if (self.y >= self.iY - walkHowMuch):
                self.y -= vel