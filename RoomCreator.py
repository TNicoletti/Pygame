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

def generateRoomBoundsFromString(r, s):
    return generateRoomBounds(int(r[0]),int(r[1]),int(r[2]),int(r[3]),s)

def generateRoomBounds(haveUp, haveDown, haveLeft, haveRight, s):
    obstaculos = []

    s = int(s)

    if (haveUp == 0):
        obstaculos.append(Platform(0, 0, int(s), int(s/80)))
    else:
        obstaculos.append(Platform(0, 0, int(s*3/8), int(s/80)))
        obstaculos.append(Platform(int(s*5/8), 0, int(s*3/8), int(s/80)))

    if (haveDown == 0):
        obstaculos.append(Platform(0, int(s-s/80), int(s), int(s/80)))
    else:
        obstaculos.append(Platform(0, int(s-s/80), int(s*3/8), int(s/80)))
        obstaculos.append(Platform(int(s*5/8), int(s-s/80), int(s*3/8), int(s/80)))

    if (haveLeft == 0):
        obstaculos.append(Platform(0, 0, int(s/80), int(s)))
    else:
        obstaculos.append(Platform(0, 0, int(s/80), int(s*3/8)))
        obstaculos.append(Platform(0, int(s*5/8), int(s/80), int(s*3/8)))

    if (haveRight == 0):
        obstaculos.append(Platform(int(s-s/80), 0, int(s/80), int(s)))
    else:
        obstaculos.append(Platform(int(s-s/80), 0, int(s/80), int(s*3/8)))
        obstaculos.append(Platform(int(s-s/80), int(s*5/8), int(s/80), int(s*3/8)))

    return obstaculos

def createRoomFromString(r,player,num,s):
    return createRoom(int(r[0]),int(r[1]),int(r[2]),int(r[3]),player,num,s)

def createRoom(haveUp, haveDown, haveLeft, haveRight, player, num,s):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight,s)

    enemies = []

    #enemies.append(Enemy(50, 50, player, obstaculos))
    #obstaculos.append(Platform(790, 0, 10, 300))

    if(num==0):
        enemies.append(MagicWarrior1(int(s*4/8), int(s*4/8), player, obstaculos,s))
    elif(num==1):
        obstaculos.append(Platform(int(s*350/800), int(s*350/800), int(s/8), int(s/8)))
        enemies.append(Enemy(int(s*150/800), int(s*4/8), player, obstaculos,s))
        enemies.append(Enemy(int(s*550/800), int(s*4/8), player, obstaculos,s))
    elif(num==2):
        obstaculos.append(Platform(int(s/16), int(s/16), int(s/16), int(s/16)))
        obstaculos.append(Platform(int(s/16), int(s*7/8), int(s/16), int(s/16)))
        obstaculos.append(Platform(int(s*7/8), int(s/16), int(s/16), int(s/16)))
        obstaculos.append(Platform(int(s*7/8), int(s*7/8), int(s/16), int(s/16)))
        enemies.append(Enemy(int(s*4/8), int(s*4/8), player, obstaculos,s))
    elif(num==3):
        obstaculos.append(Platform(int(s*3/8), int(s*3/8), int(s*200/800), int(s*200/800)))
        enemies.append(Patocomarmaebandana(int(s/8), int(s/8), player, obstaculos,s))
        enemies.append(Enemy(int(s*7/8), int(s*7/8), player, obstaculos,s))
    elif(num==4):
        obstaculos.append(Platform(int(s*175/800), int(s*375/800), int(s*450/800), int(s/16)))
        obstaculos.append(Platform(int(s*375/800), int(s*175/800), int(s/16), int(s*450/800)))
        enemies.append(Enemy(int(s*250/800), int(s*550/800), player, obstaculos,s))
        enemies.append(Patocomarma(int(s*250/800), int(s*250/800), player, obstaculos,s))
        enemies.append(Enemy(int(s*550/800), int(s*550/800), player, obstaculos,s))
        enemies.append(Enemy(int(s*550/800), int(s*250/800), player, obstaculos,s))
    elif(num==5):
        enemies.append(Enemy(int(s*250/800), int(s*550/800), player, obstaculos,s))
        enemies.append(Patocomarmaebandana(int(s*250/800), int(s*250/800), player, obstaculos,s))
        enemies.append(Enemy(int(s*550/800), int(s*550/800), player, obstaculos,s))
        enemies.append(Patocomarma(int(s*550/800), int(s*250/800), player, obstaculos,s))
        enemies.append(Enemy(int(s*350/800), int(s*350/800), player, obstaculos,s))
    elif(num==6):
        obstaculos.append(Platform(0, 0, int(s*3/8), int(s*3/8)))
        obstaculos.append(Platform(int(s*5/8), 0, int(s*3/8), int(s*3/8)))
        obstaculos.append(Platform(0, int(s*5/8), int(s*3/8), int(s*3/8)))
        obstaculos.append(Platform(int(s*5/8), int(s*5/8), int(s*3/8), int(s*3/8)))
        enemies.append(Patocomarma(int(s*350/800), int(s*350/800), player, obstaculos,s))
    elif(num==7):
        for i in range(1,8):
            for j in range(1,8):
                obstaculos.append(Platform(int(s/8)*i, int(s/8)*j, int(s/80), int(s/80)))
        enemies.append(MagicWarrior1(int(s*41/80), int(s*41/80), player, obstaculos,s))
    elif(num==8):
        pass
    elif(num==9):
        pass



    shops = []

    return mapSlice(enemies, obstaculos, shops, 1, str(haveUp)+str(haveDown)+str(haveLeft)+str(haveRight))

def createInitialRoomFromString(r,s):
    return createInitialRoom(int(r[0]),int(r[1]),int(r[2]),int(r[3]),s)

def createInitialRoom(haveUp, haveDown, haveLeft, haveRight,s):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight,s)

    enemies = []

    shops = []

    return mapSlice(enemies, obstaculos, shops, 0, str(haveUp)+str(haveDown)+str(haveLeft)+str(haveRight))

def createShopRoomFromString(r,player,s):
    return createShopRoom(int(r[0]),int(r[1]),int(r[2]),int(r[3]),player,s)

def createShopRoom(haveUp, haveDown, haveLeft, haveRight, player,s):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight,s)

    enemies = []

    shops = [Shop(int(s*7/8), int(s*7/8), Gun(5, 2, player, "minigum"), 2000, player),
             Shop(int(s*7/8), int(s/80), Gun(500, 2 * 60, player, "exploder"), 3000, player)]

    return mapSlice(enemies, obstaculos, shops, 2, str(haveUp)+str(haveDown)+str(haveLeft)+str(haveRight))

def createBossRoom(r,player,s):
    obstaculos = generateRoomBounds(r[0]=="1", r[1]=="1", r[2]=="1", r[3]=="1",s)
    enemies = [TheFirstBoss(int(s/16),int(s/16),player,obstaculos,s)]
    shops = []
    return mapSlice(enemies,obstaculos,shops,3,r)