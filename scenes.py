import pygame
from pygame.locals import *
from sprites import *
from abc import ABC, abstractmethod
from pathlib import Path


class Scene(ABC):
    @abstractmethod
    def view(self, screen: pygame.Surface, clock: pygame.time.Clock, game: Game): ...


class GameScene(Scene):
    def __init__(self):
        self.player = Player()
        self.bombs = [Bomb()]

    def view(
        self, screen: pygame.Surface, clock: pygame.time.Clock, game: Game
    ) -> Scene:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        self.player.update()
        self.player.draw(screen)
        for bomb in self.bombs:
            bomb.fall()
            bomb.draw(screen)
            if bomb.rect.colliderect(self.player.rect):
                game.scene = TitleScene()

        pygame.display.update()
        clock.tick(60)


class TitleScene(Scene):
    def __init__(self):
        self.playText = Font.neodgm36.render("게임 시작", False, (255, 255, 255))
        self.playTextRect = self.playText.get_rect(center=(300, 275))
        self.hoverPlayText = Font.neodgm36.render("> 게임 시작", False, (255, 255, 255))
        self.hoverPlayTextRect = self.hoverPlayText.get_rect(center=(300, 275))

        self.tutorialText = Font.neodgm36.render("튜토리얼", False, (255, 255, 255))
        self.tutorialTextRect = self.tutorialText.get_rect(center=(300, 375))
        self.hoverTutorialText = Font.neodgm36.render(
            "> 튜토리얼", False, (255, 255, 255)
        )
        self.hoverTutorialTextRect = self.hoverTutorialText.get_rect(center=(300, 375))

        self.quitText = Font.neodgm36.render("나가기", False, (255, 255, 255))
        self.quitTextRect = self.quitText.get_rect(center=(300, 475))
        self.hoverQuitText = Font.neodgm36.render("> 나가기", False, (255, 255, 255))
        self.hoverQuitTextRect = self.hoverQuitText.get_rect(center=(300, 475))

    def view(
        self, screen: pygame.Surface, clock: pygame.time.Clock, game: Game
    ) -> Scene:
        screen.fill(BLACK)
        # 플레이, 설정, 튜토리얼 버튼 3가지

        isLMouseClicked = pygame.mouse.get_pressed()[0]

        if isMouseInRect(self.playTextRect):  # 플레이 버튼 클릭
            screen.blit(self.hoverPlayText, self.hoverPlayTextRect)
            if isLMouseClicked:
                game.scene = GameScene()
        else:
            screen.blit(self.playText, self.playTextRect)

        if isMouseInRect(self.tutorialTextRect):  # 튜토리얼 버튼 클릭
            screen.blit(self.hoverTutorialText, self.hoverTutorialTextRect)
        else:
            screen.blit(self.tutorialText, self.tutorialTextRect)

        if isMouseInRect(self.quitTextRect):  # 나가기 버튼 클릭
            screen.blit(self.hoverQuitText, self.hoverQuitTextRect)
            if isLMouseClicked:
                game.running = False
        else:
            screen.blit(self.quitText, self.quitTextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        pygame.display.update()
        clock.tick(60)


class TutorialScene(Scene):
    def view(
        self, screen: pygame.Surface, clock: pygame.time.Clock, game: Game
    ) -> Scene:
        game.scene = TitleScene()


def isMouseInRect(rect: pygame.Rect):
    mousePos = pygame.mouse.get_pos()
    if (
        (rect.left <= mousePos[0])
        and (mousePos[0] <= rect.right)
        and (rect.top <= mousePos[1])
        and (mousePos[1] <= rect.bottom)
    ):
        return True
