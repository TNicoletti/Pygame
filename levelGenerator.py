import pygame
from mapSlice import *
from shop import *
from gun import *
from platform import *
import random
from RoomCreator import *

class levelGenerator():
    def __init__(self,player,seed):
        self.level = 0

        self.player = player

        self.map = 0
        self.tela = [25, 25]

        self.generateFloor(seed)


    def generateFloor(self, seed):

        #print("a")
        self.map = []
        for i in range(50):
            self.map.append([])

            for j in range(50):
                self.map[i].append(None)

        numFloors = 15
        if(self.level == 2):
            numFloors += 5


        salas = [[25,25]]
        i = 0
        j = 0

        #while(len(salas)<10):
        for dfadsfsdf in range(10):
            #char to int
            a = ord(seed[i])-ord('a')
            #ordSala = '{:04b}'.format(a % 16)
            ordSala = '{:04b}'.format(a)

            #print(ordSala)
            if(ordSala[0]=="1"):
                salas.append([salas[j][0]-1,salas[j][1]])
            if(ordSala[1]=="1"):
                salas.append([salas[j][0]+1,salas[j][1]])
            if(ordSala[2]=="1"):
                salas.append([salas[j][0],salas[j][1]-1])
            if(ordSala[3]=="1"):
                salas.append([salas[j][0],salas[j][1]+1])
            
            if(a%16!=0):
                j+=1
            i+=1
            if(i==len(seed)):
                i=0

        aux = []
        for s in salas:
            c = str(s)
            if c not in aux:
                aux.append(c)
            #print(coisa)
        salas = aux

        shops = ord(seed[i])-ord('a')
        i+=1
        if(i==len(seed)):
            i=0

        boss = False

        for s in salas:
            c = s[1:7].split(", ")
            setup = ['0','0','0','0']
            
            if str([int(c[0])-1,int(c[1])]) in salas:
                setup[0]='1'
            if str([int(c[0])+1,int(c[1])]) in salas:
                setup[1]='1'
            if str([int(c[0]),int(c[1])-1]) in salas:
                setup[2]='1'
            if str([int(c[0]),int(c[1])+1]) in salas:
                setup[3]='1'
            qtd = sum([int(x) for x in setup])

            #print(setup)
            setup = "".join(setup)
            #print(setup)

            if(s==str([25,25])):
                self.map[25][25] = createInitialRoomFromString(setup)
                #print("add sala inici")
            elif(shops==0):
                self.map[int(c[0])][int(c[1])] = createShopRoomFromString(setup,self.player)
                #print("add shop")
            elif(qtd==1 and boss==False):
                boss=True
                self.map[int(c[0])][int(c[1])] = createBossRoom(setup,self.player)                
            else:
                self.map[int(c[0])][int(c[1])] = createRoomFromString(setup,self.player,(ord(seed[i])-ord('a'))%8)
                #print("add sala")
            
            if(ord(seed[i])-ord('a')<15):
                seed = seed[:i]+chr(ord(seed[i])+1)+seed[i+1:]
            else:
                seed = seed[:i-1]+'a'+seed[i:]
            i+=1
            if(i==len(seed)):
                i=0

            shops-=1
        
        #self.map[25][25] = createInitialRoom(1, 1, 0, 0)
        #self.map[24][25] = createRoom(0, 1, 0, 0, self.player)
        #self.map[26][25] = createShopRoom(1, 0, 0, 0, self.player)

        '''for i in range(numFloors - 1):
            if(random.randInt(1, numFloors - i >= 4)):
                map[25][25] = mapSlice([], [], [Shop(700, 700, Gun(50, 2, self.player), 0, self.player),
                                            Shop(700, 10, Gun(1500, 5 * 60, self.player), 3000, self.player)])'''


    def getAtualMap(self):
        return self.map[self.tela[0]][self.tela[1]]

    def marcarVisto(self):
        at = self.getAtualMap()
        at.visto = 1
        at = at.doors
        if(at[0]=="1" and self.map[self.tela[0]-1][self.tela[1]].visto==0):
            self.map[self.tela[0]-1][self.tela[1]].visto = 2
        if(at[1]=="1" and self.map[self.tela[0]+1][self.tela[1]].visto==0):
            self.map[self.tela[0]+1][self.tela[1]].visto = 2
        if(at[2]=="1" and self.map[self.tela[0]][self.tela[1]-1].visto==0):
            self.map[self.tela[0]][self.tela[1]-1].visto = 2
        if(at[3]=="1" and self.map[self.tela[0]][self.tela[1]+1].visto==0):
            self.map[self.tela[0]][self.tela[1]+1].visto = 2
        return

    def changeSlice(self, where):

        if(where == "u"):
            self.tela[0] -= 1
        elif(where == "d"):
            self.tela[0] += 1
        elif(where == "l"):
            self.tela[1] -= 1
        elif(where == "r"):
            self.tela[1] += 1        

        return self.map[self.tela[0]][self.tela[1]]
