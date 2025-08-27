#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_HEIGHT
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position)
        self.speed = speed

    def move(self, ):
        self.rect.centery += self.speed
        if self.rect.top >= WIN_HEIGHT:
            self.rect.y = self.rect.y - 2 * self.rect.height
        pass