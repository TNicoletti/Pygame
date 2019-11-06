import pygame
from platform import *

class mapSlice():
    def __init__(self, enemies, obstaculos, shops):
        self.enemies = enemies
        self.obstaculos = obstaculos
        self.shops = shops