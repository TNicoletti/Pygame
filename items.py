import pygame


class Item(object):
    def __init__(self, x, y, player, s):
        self.x = x
        self.y = y
        self.width = int(s/16) #50
        self.height = int(s*7/80) #70
        self.vel = int(s*3/800) #3

        self.player = player

    def draw(self, win, s):
        pygame.draw.rect(win, (50, 50, 50), (self.x, self.y, self.width, self.height))

    def confereMargem(self, *args):
        if (len(args) == 1):
            x = args[0].x
            y = args[0].y
            height = args[0].height
            width = args[0].width
        else:
            x = args[0].x
            y = args[1].y
            width = args[2].width
            height = args[3].height

        if (self.x + self.width > x and self.x < x + width):
            if (self.y + self.height > y and self.y < y + height):
                return True

        return False

    def get(self, player):
        player.life += 1

    def selfDestroy(self, player):
        player.items.remove(self)