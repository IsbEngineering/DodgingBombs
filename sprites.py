from preset import *
from pathlib import Path
import random


characterImage = pygame.transform.scale(
    pygame.image.load(Path(__file__).parent / Path("images/character.png")), (100, 100)
)
bombImage = pygame.transform.scale(
    pygame.image.load(Path(__file__).parent / Path("images/bomb.png")), (50, 50)
)


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
