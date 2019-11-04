import pygame

class Enemy(object):
    def __init__(self, x, y, player, platforms):
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

        self.platforms = platforms

        #self.g = gravity

        #self.hitbox = (self.x, self.y, self.width, self.height)

        self.ori = "right"

        self.life = 200

        self.attackCoul = 0

    def draw(self, win):
        pygame.draw.rect(win, (68, 117, 72), (self.x, self.y, self.width, self.height))

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

        if(self.y < self.player.y):
            self.y += self.vel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y -= self.vel
                    break
        elif(self.y > self.player.y):
            self.y -= self.vel

            for p in self.platforms:
                if (self.confereMargem(p)):
                    self.y += self.vel
                    break

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
            self.player.takeDamage(1)
            self.attackCoul = 0