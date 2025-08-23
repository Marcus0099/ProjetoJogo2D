#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position) #RETORNO

    def move(self, ):
        self.rect.centery += ENTITY_SPEED[self.name]
        if self.rect.top >= WIN_HEIGHT:
            self.rect.y = self.rect.y - 2 * self.rect.height
        pass
