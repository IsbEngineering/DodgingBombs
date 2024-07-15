import pygame
from pygame.locals import *
from pathlib import Path

# 색 정의
BLUE = pygame.Color(0, 0, 255)
RED = pygame.Color(255, 0, 0)
GREEN = pygame.Color(0, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

# 창 크기
windowSize = [600, 800]

# 폰트
pygame.font.init()


class Font:
    neodgm36 = pygame.font.Font(Path(__file__).parent / Path("fonts/neodgm.ttf"), 36)


# 게임 내 데이터를 모아두는 자료구조
class Game:
    scene = None
    running = True
