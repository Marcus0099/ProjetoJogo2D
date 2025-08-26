import random

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position)
        self.speed = speed

    def move(self):
        self.rect.centery += self.speed
