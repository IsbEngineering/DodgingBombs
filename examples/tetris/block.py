from typing import Tuple
import pygame

ColorValue = Tuple[int, int, int]
Coordinate = Tuple[int, int]


class Block:
    def __init__(self):
        self.center: Coordinate = ()
        self.shape: list[Coordinate] = []
        self.color: ColorValue = ()

    def fall(self): ...
