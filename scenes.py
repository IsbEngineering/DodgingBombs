from sprites import *
from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self):
        self.isOnScreen = True

    @abstractmethod
    def view(self, screen: pygame.Surface, clock: pygame.time.Clock): ...


class GameScene(Scene):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.bombs = [Bomb()]

    def view(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None:
        screen.fill(BLACK)  # 배경

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isOnScreen = False

        self.player.update()
        self.player.draw(screen)
        for bomb in self.bombs:
            bomb.fall()
            bomb.draw(screen)
            if bomb.rect.colliderect(self.player.rect):
                self.isOnScreen = False

        pygame.display.update()
        clock.tick(60)


class TitleScene(Scene):
    def __init__(self):
        super().__init__()

    def view(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None: ...

class TutorialScene(Scene):
    def __init__(self):
        super().__init__()
    
    def view(self, screen: pygame.Surface, clock: pygame.time.Clock) -> None: ...


if __name__ == "__main__":  # 디버그 코드
    ts = TitleScene()
    print(ts.isOnScreen)
