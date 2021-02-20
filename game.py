import pygame
from inc.background import Background
from inc.sprites.reactor import Reactor
from inc.sprites.progressbarwater import ProgressWater
from inc.sprites.progressbarheat import ProgressHeat
from inc.sprites.buttonwater import ButtonWater

class Game():
    def __init__(self):
        self.background = Background()
        self.reactor = Reactor()
        self.progresswater = ProgressWater()
        self.progressheat = ProgressHeat()
        self.buttonwater = ButtonWater()

        self.stop = False
