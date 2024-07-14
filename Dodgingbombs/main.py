import pygame
from pygame.locals import *
import random
from pathlib import Path

pygame.init()

# 기본 설정
windowSize = [600, 800]
screen = pygame.display.set_mode(windowSize)

# 이미지
chrImagePath = Path(__file__).parent / Path("images/character.png")
characterImage = pygame.transform.scale(pygame.image.load(chrImagePath), (100, 100))
bombImagePath = Path(__file__).parent / Path("images/bomb.png")
bombImage = pygame.transform.scale(pygame.image.load(bombImagePath), (50, 50))

# 색
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# 스프라이트
class Bomb(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = bombImage
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 600 - 40), 0)

    def fall(self) -> None:
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 800:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 600 - 30), 0)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = characterImage
        self.rect = self.image.get_rect()
        self.rect.center = (windowSize[0] // 2, 750)

    def update(self) -> None:
        isPressed = pygame.key.get_pressed()

        if self.rect.left > 0 and isPressed[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < windowSize[0] and isPressed[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.image, self.rect)


running = True
clock = pygame.time.Clock()

player = Player()
bombs = [Bomb()]


def runGame():
    global running
    while running:
        screen.fill(BLACK)  # 배경

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        player.draw(screen)
        for bomb in bombs:
            bomb.fall()
            bomb.draw(screen)
            if bomb.rect.colliderect(player.rect):
                running = False

        pygame.display.update()
        clock.tick(60)


runGame()
pygame.quit()
