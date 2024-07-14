from preset import *
from scenes import GameScene

pygame.init()

screen = pygame.display.set_mode(windowSize)

clock = pygame.time.Clock()

gameScene = GameScene()


def runGame():
    running = True
    while running:
        while gameScene.isOnScreen:
            gameScene.view(screen, clock)
        running = False


runGame()
pygame.quit()
