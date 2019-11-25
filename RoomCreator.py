from enemy import *
import random
from platform import *
from mapSlice import *
from shop import *
from gun import *
from MagicWarrior1 import *
from TheFirstBoss import *
from patocomarma import *
from patocomarmaebandana import *

from patocomarma import *

def generateRoomBoundsFromString(r):
    return generateRoomBounds(int(r[0]),int(r[1]),int(r[2]),int(r[3]))

def generateRoomBounds(haveUp, haveDown, haveLeft, haveRight):
    obstaculos = []

    if (haveUp == 0):
        obstaculos.append(Platform(0, 0, 800, 10))
    else:
        obstaculos.append(Platform(0, 0, 300, 10))
        obstaculos.append(Platform(500, 0, 300, 10))

    if (haveDown == 0):
        obstaculos.append(Platform(0, 790, 800, 10))
    else:
        obstaculos.append(Platform(0, 790, 300, 10))
        obstaculos.append(Platform(500, 790, 300, 10))

    if (haveLeft == 0):
        obstaculos.append(Platform(0, 0, 10, 800))
    else:
        obstaculos.append(Platform(0, 0, 10, 300))
        obstaculos.append(Platform(0, 500, 10, 300))

    if (haveRight == 0):
        obstaculos.append(Platform(790, 0, 10, 800))
    else:
        obstaculos.append(Platform(790, 0, 10, 300))
        obstaculos.append(Platform(790, 500, 10, 300))

    return obstaculos

def createRoomFromString(r,player,num):
    return createRoom(int(r[0]),int(r[1]),int(r[2]),int(r[3]),player,num)

def createRoom(haveUp, haveDown, haveLeft, haveRight, player, num):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight)

    enemies = []

    #enemies.append(Enemy(50, 50, player, obstaculos))
    #obstaculos.append(Platform(790, 0, 10, 300))

    if(num==0):
        enemies.append(Patocomarmaebandana(400, 400, player, obstaculos))
    elif(num==1):
        obstaculos.append(Platform(350, 350, 100, 100))
        enemies.append(Enemy(150, 400, player, obstaculos))
        enemies.append(Enemy(550, 400, player, obstaculos))
    elif(num==2):
        obstaculos.append(Platform(50, 50, 50, 50))
        obstaculos.append(Platform(50, 700, 50, 50))
        obstaculos.append(Platform(700, 50, 50, 50))
        obstaculos.append(Platform(700, 700, 50, 50))
        enemies.append(Enemy(400, 400, player, obstaculos))
    elif(num==3):
        obstaculos.append(Platform(300, 300, 200, 200))
        enemies.append(Enemy(100, 100, player, obstaculos))
        enemies.append(Enemy(700, 700, player, obstaculos))
    elif(num==4):
        obstaculos.append(Platform(175, 375, 450, 50))
        obstaculos.append(Platform(375, 175, 50, 450))
        enemies.append(Enemy(250, 550, player, obstaculos))
        enemies.append(Enemy(250, 250, player, obstaculos))
        enemies.append(Enemy(550, 550, player, obstaculos))
        enemies.append(Enemy(550, 250, player, obstaculos))
    elif(num==5):
        enemies.append(Enemy(250, 550, player, obstaculos))
        enemies.append(Enemy(250, 250, player, obstaculos))
        enemies.append(Enemy(550, 550, player, obstaculos))
        enemies.append(Enemy(550, 250, player, obstaculos))
        enemies.append(Enemy(350, 350, player, obstaculos))
    elif(num==6):
        obstaculos.append(Platform(0, 0, 300, 300))
        obstaculos.append(Platform(500, 0, 300, 300))
        obstaculos.append(Platform(0, 500, 300, 300))
        obstaculos.append(Platform(500, 500, 300, 300))
        enemies.append(Enemy(350, 350, player, obstaculos))
    elif(num==7):
        for i in range(1,8):
            for j in range(1,8):
                obstaculos.append(Platform(100*i, 100*j, 10, 10))
        enemies.append(Enemy(410, 410, player, obstaculos))



    shops = []

    return mapSlice(enemies, obstaculos, shops, 1, str(haveUp)+str(haveDown)+str(haveLeft)+str(haveRight))

def createInitialRoomFromString(r):
    return createInitialRoom(int(r[0]),int(r[1]),int(r[2]),int(r[3]))

def createInitialRoom(haveUp, haveDown, haveLeft, haveRight):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight)

    enemies = []

    shops = []

    return mapSlice(enemies, obstaculos, shops, 0, str(haveUp)+str(haveDown)+str(haveLeft)+str(haveRight))

def createShopRoomFromString(r,player):
    return createShopRoom(int(r[0]),int(r[1]),int(r[2]),int(r[3]),player)

def createShopRoom(haveUp, haveDown, haveLeft, haveRight, player):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight)

    enemies = []

    shops = [Shop(700, 700, Gun(5, 2, player, "minigum"), 2000, player),
             Shop(700, 10, Gun(500, 2 * 60, player, "exploder"), 3000, player)]

    return mapSlice(enemies, obstaculos, shops, 2, str(haveUp)+str(haveDown)+str(haveLeft)+str(haveRight))

def createBossRoom(r,player):
    obstaculos = generateRoomBounds(r[0]=="1", r[1]=="1", r[2]=="1", r[3]=="1")
    enemies = [TheFirstBoss(50,50,player,obstaculos)]
    shops = []
    return mapSlice(enemies,obstaculos,shops,3,r)