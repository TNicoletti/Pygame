import pygame

class Shop(object):
    def __init__(self, x, y, gun, price, player):
        self.x = x
        self.y = y
        self.width  = 50
        self.height = 70
        self.vel = 3

        self.player = player

        self.price = price
        self.gun = gun

    def draw(self, win):
        pygame.draw.rect(win, (122, 140, 118), (self.x, self.y, self.width, self.height))
        
    def confereMargem(self, *args):
        if(len(args) == 1):
            x = args[0].x
            y = args[0].y
            height = args[0].height
            width = args[0].width
        else:
            x = args[0].x
            y = args[1].y
            width = args[2].width
            height = args[3].height

        if(self.x + self.width > x and self.x < x + width):
            if(self.y + self.height > y and self.y < y + height):
                return True

        return False

    def buy(self):
        if(self.confereMargem(self.player)):
            if(self.player.points >= self.price):
                self.player.points -= self.price
                self.player.changeGun(self.gun)