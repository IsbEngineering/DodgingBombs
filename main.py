import pygame
from preset import Data
from scenes import *

pygame.init()

data = Data()
data.scene = TitleScene()
screen = pygame.display.set_mode(data.windowSize)

clock = pygame.time.Clock()

def runGame():
    while data.running:
        data.scene.view(screen, clock, data)

runGame()
pygame.quit()
