import pygame
from mapSlice import *
from shop import *
from gun import *
from platform import *
import random
from RoomCreator import createRoom, createInitialRoom, createShopRoom

class levelGenerator():
    def __init__(self,player):
        self.level = 0

        self.player = player

        self.map = 0
        self.tela = [25, 25]

        self.generateFloor()


    def generateFloor(self):

        #print("a")
        self.map = []
        for i in range(50):
            self.map.append([])

            for j in range(50):
                self.map[i].append(None)


        numFloors = 15

        if(self.level == 2):
            numFloors += 5

        self.map[25][25] = createInitialRoom(1, 0, 0, 0)
        self.map[24][25] = createRoom(0, 1, 0, 0, self.player)

        '''for i in range(numFloors - 1):
            if(random.randInt(1, numFloors - i >= 4)):
                map[25][25] = mapSlice([], [], [Shop(700, 700, Gun(50, 2, self.player), 0, self.player),
                                            Shop(700, 10, Gun(1500, 5 * 60, self.player), 3000, self.player)])'''


    def getAtualMap(self):
        return self.map[self.tela[0]][self.tela[1]]

    def changeSlice(self, where):

        if(where == "u"):
            self.tela[0] -= 1
        elif(where == "d"):
            self.tela[0] += 1
        elif(where == "l"):
            self.tela[1] -= 1
        else:
            self.tela[1] += 1

        print(self.tela[0])
        print(self.tela[1])

        return self.map[self.tela[0]][self.tela[1]]
