import pygame

class Enemy(object):
    def __init__(self, x, y, player, gravity):
        self.x = x
        self.y = y
        self.width  = 50
        self.height = 50
        self.vel = 3

        self.tickTime = 0
        self.clockTick = 60

        self.player = player

        self.jumpped = False
        self.jumpForce = -15

        self.yVel = 0
        self.landded = False

        self.g = gravity

        #self.hitbox = (self.x, self.y, self.width, self.height)

        self.ori = "right"

        self.platforms = []

        self.life = 1000

        self.attackCoul = 0

    def draw(self, win):
        pygame.draw.rect(win, (68, 117, 72), (self.x, self.y, self.width, self.height))

    def commitLandded(self, platforms):
        self.platforms = platforms
        for p in platforms: 
            if(self.confereMargem(p) == True):
                if(self.yVel > 0):
                    self.y = p.y - self.height
                    self.yVel = 0
                    self.landded = True
                elif(self.yVel < 0):
                    self.y = p.y + p.height
                    self.yVel = 0
                return
        
        self.landded = False

    def move(self):

        self.tickTime += 1
        normalTime = self.tickTime / self.clockTick

        if(self.x > self.player.x):
            self.x -= self.vel
            self.ori = "left"
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.x += self.vel
                    if (not self.jumpped):
                        self.yVel += self.jumpForce
                        self.jumpped = True
                    break

        else:
            self.x += self.vel
            self.ori = "right"
            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.x -= self.vel
                    if (not self.jumpped):
                        self.yVel += self.jumpForce
                        self.jumpped = True
                    break

        if(self.y > self.player.y):
            if (not self.jumpped):
                self.yVel += self.jumpForce
                self.jumpped = True

        if(not self.landded): 
            self.yVel += self.g
        else:
            self.yVel = 0
            self.jumpped = False

        self.y += self.yVel

        if(normalTime % 1 == 0):
            self.attackCoul += 1
        
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

    def takeDamage(self, damage):
        self.life -= damage

    def do_attack(self):

        if(self.confereMargem(self.player) and self.attackCoul >= 1):
            self.player.takeDamage(50)
            self.attackCoul = 0