import pygame
import assets
import random

pygame.init()

windowSize = [600, 800]
screen = pygame.display.set_mode(windowSize)

running = True
clock = pygame.time.Clock()

def runGame():
    global running
    while running:
        clock.tick(10)
        screen.fill(assets.BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()


runGame()
pygame.quit()