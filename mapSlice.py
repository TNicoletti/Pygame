import pygame
from platform import *

class mapSlice():
    def __init__(self, enemies, obstaculos, shops, tipo, doors):
        self.enemies = enemies
        self.obstaculos = obstaculos
        self.shops = shops
        self.tipo = tipo 
        #0 = inicio
        #1 = normal
        #2 = shop
        #3 = boss?
        self.visto = 0
        self.doors = doors