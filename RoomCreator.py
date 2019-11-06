from enemy import *
import random
from platform import *
from mapSlice import *

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

def createRoom(haveUp, haveDown, haveLeft, haveRight, player):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight)

    enemies = []
    enemies.append(Enemy(50, 50, player, obstaculos))

    enemies.append(Enemy(50, 600, player, obstaculos))

    enemies.append(Enemy(600, 50, player, obstaculos))

    enemies.append(Enemy(600, 600, player, obstaculos))

    shops = []

    return mapSlice(enemies, obstaculos, shops)

def createInitialRoom(haveUp, haveDown, haveLeft, haveRight):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight)

    enemies = []

    shops = []

    return mapSlice(enemies, obstaculos, shops)

def createShopRoom(haveUp, haveDown, haveLeft, haveRight):
    obstaculos = generateRoomBounds(haveUp, haveDown, haveLeft, haveRight)

    enemies = []

    shops = [Shop(700, 700, Gun(50, 2, self.player), 0, self.player),
             Shop(700, 10, Gun(1500, 5 * 60, self.player), 3000, self.player)]

    return mapSlice(enemies, obstaculos, shops)