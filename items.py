import pygame


class Item(object):
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 70
        self.vel = 3

        self.player = player

    def draw(self, win):
        pygame.draw.rect(win, (150, 150, 150), (self.x, self.y, self.width, self.height))

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