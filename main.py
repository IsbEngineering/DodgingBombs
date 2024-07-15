import pygame
from preset import *
from scenes import *

pygame.init()

screen = pygame.display.set_mode(windowSize)

clock = pygame.time.Clock()

gameScene = GameScene()
titleScene = TitleScene()
tutorialScene = TutorialScene()

def runGame():
    running = True
    while running:
        while gameScene.isOnScreen:
            gameScene.view(screen, clock)
        running = False


runGame()
pygame.quit()
