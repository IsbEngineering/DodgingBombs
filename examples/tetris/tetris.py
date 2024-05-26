import pygame
import os
from typing import Tuple
from random import randint
import block

os.chdir(os.path.split(__file__)[0])
ColorValue = Tuple[int, int, int]
Coordinate = Tuple[int, int]


def getText(text: str, font: str, size: int, color: ColorValue) -> pygame.Surface:
    sysfont = pygame.font.SysFont(font, size)
    return sysfont.render(
        text,
        True,
        color,
    )


pygame.init()
done = False
size = [600, 800]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

bg = pygame.image.load("./imgs/background.png")
texts = {}
texts["next"] = getText("next", "AppleSDGothicNeoSB00", 36, (255, 255, 255))
texts["SCORE"] = getText("SCORE", "AppleSDGothicNeoSB00", 36, (255, 255, 255))
score = getText("00000", "AppleSDGothicNeoSB00", 36, (255, 255, 255))


class Room:
    def __init__(self, color: ColorValue, rect: pygame.rect.Rect):
        self.color = color
        self.rect = rect


class Field:
    def __init__(self):
        # (0, 0) 부터 (7, 14)까지
        self.rooms: list[list[Room]] = [[() for i in range(15)] for i in range(8)]
        for x in range(8):
            for y in range(15):
                self.rooms[x][y] = Room(
                    (0, 0, 0), pygame.rect.Rect(17 + 50 * x, 734 - 50 * y, 50, 50)
                )

    def changeRoomColor(self, coord: Coordinate, color: ColorValue):
        x, y = coord
        self.rooms[x][y].color = color

    def refresh(self):
        for line in self.rooms:
            for room in line:
                pygame.draw.rect(screen, room.color, room.rect)


def runGame() -> None:
    global done
    field = Field()

    while not done:
        clock.tick(1000)
        screen.blit(bg, (0, 0))
        screen.blit(texts["next"], (467, 20))
        screen.blit(texts["SCORE"], (450, 220))
        screen.blit(score, (447, 256))

        pygame.draw.rect(screen, (255, 255, 255), (17, 734 - 50 * 14, 50, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        field.refresh()
        pygame.display.update()


runGame()
pygame.quit()
