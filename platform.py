import pygame

class Platform(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width  = width
        self.height = height

        self.vel = 0

        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))


    def move(self):
        pass

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