import pygame
from preset import Game
from scenes import *

pygame.init()

game = Game()
game.scene = TitleScene()
screen = pygame.display.set_mode(windowSize)

clock = pygame.time.Clock()


def runGame():
    while game.running:
        game.scene.view(screen, clock, game)


runGame()
pygame.quit()
