import pygame
from inc.background import Background
from inc.sprites.reactor import Reactor
from inc.sprites.progressbarwater import ProgressWater

class Game():
    def __init__(self):
        self.background = Background()
        self.reactor = Reactor()
        self.progresswater = ProgressWater()
