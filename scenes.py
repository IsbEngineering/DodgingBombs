from sprites import Data
from abc import ABC, abstractmethod


class Scene(ABC):;
    @abstractmethod
    def view(self, screen: pygame.Surface, clock: pygame.time.Clock, data: Data) -> Scene: ...


class GameScene(Scene):
    def __init__(self):
        self.player = Player()
        self.bombs = [Bomb()]

    def view(self, screen: pygame.Surface, clock: pygame.time.Clock, data: Data) -> Scene:
        screen.fill(BLACK)  # 배경

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data.scene = TitleScene()

        self.player.update()
        self.player.draw(screen)
        for bomb in self.bombs:
            bomb.fall()
            bomb.draw(screen)
            if bomb.rect.colliderect(self.player.rect):
                data.scene = TitleScene()

        pygame.display.update()
        clock.tick(60)


class TitleScene(Scene):
    def view(self, screen: pygame.Surface, clock: pygame.time.Clock, data: Data) -> Scene:
        data.scene = GameScene()

class TutorialScene(Scene):
    def view(self, screen: pygame.Surface, clock: pygame.time.Clock, data: Data) -> Scene:
        data.scene = TitleScene()

if __name__ == "__main__":  # 디버그 코드
    ts = TitleScene()
    print(ts.isOnScreen)
