import pygame
from pathlib import Path

# 이미지
chrImagePath = Path(__file__).parent / Path("images/character.png")
characterImage = pygame.image.load(chrImagePath)


# 색
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# 클래스
class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        pass