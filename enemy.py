import pygame

class Enemy(object):
    def __init__(self, x, y, player, platforms):
        self.x = x
        self.y = y
        self.width  = 50 #TODO dinamic
        self.height = 50 #TODO dinamic
        self.xVel = 3    #TODO dinamic
        self.yVel = 0    #TODO dinamic

        self.tickTime = 0
        self.clockTick = 60

        self.player = player

        self.jumped = False
        self.jumpForce = -15 #TODO dinamic

        #self.landded = False

        self.platforms = platforms

        #self.g = gravity

        #self.hitbox = (self.x, self.y, self.width, self.height)

        self.ori = "right"

        self.life = 200

        self.attackCool = 0

    def draw(self, win):      #TODO dinamic
        pygame.draw.rect(win, (68, 117, 72), (self.x, self.y, self.width, self.height))

    def move(self):

        self.tickTime += 1
        normalTime = self.tickTime / self.clockTick

        if(self.x > self.player.x):
            self.x -= self.xVel
            self.ori = "left"
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.x += self.xVel
                    if (not self.jumped):
                        self.yVel += self.jumpForce
                        self.jumped = True
                    break

        else:
            self.x += self.xVel
            self.ori = "right"
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.x -= self.xVel
                    if (not self.jumped):
                        self.yVel += self.jumpForce
                        self.jumped = True
                    break

        if(self.y < self.player.y):
            self.y += self.xVel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y -= self.xVel
                    break
        elif(self.y > self.player.y):
            self.y -= self.xVel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y += self.xVel
                    break

        if(normalTime % 1 == 0):
            self.attackCool += 1
        
    def confereMargem(self, *args):
        if(len(args) == 1):
            px = args[0].x
            py = args[0].y
            height = args[0].height
            width = args[0].width
        else:
            px = args[0].x
            py = args[1].y
            width = args[2].width
            height = args[3].height

        if(self.x + self.width > px and self.x < px + width):
            if(self.y + self.height > py and self.y < py + height):
                return True

        return False

    def takeDamage(self, damage):
        self.life -= damage

    def do_attack(self):

        if(self.confereMargem(self.player) and self.attackCool >= 1):
            self.player.takeDamage(1)
            self.attackCool = 0