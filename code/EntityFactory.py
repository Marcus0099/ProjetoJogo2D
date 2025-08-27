#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                speed = 8
                bg_name = 'Level1Bg0'  # só uma imagem
                for copy in range(2):  # duas cópias para loop
                    y = copy * WIN_HEIGHT
                    list_bg.append(Background(bg_name, (0, y), speed))
                return list_bg
            case 'Player1Car':
                return Player('Player1Car', (WIN_WIDTH // 2 - 90, WIN_HEIGHT - 150))
            case 'Player2Car':
                return Player('Player2Car', (WIN_WIDTH // 2 + 40, WIN_HEIGHT - 150))
            case 'Enemy1Car':
                return Enemy('Enemy1Car', (WIN_HEIGHT - 10, random.randint(10, WIN_WIDTH)))
            case 'Enemy2Car':
                return Enemy('Enemy2Car', (WIN_HEIGHT - 10, random.randint(10, WIN_WIDTH)))
