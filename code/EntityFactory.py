#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = [] # Se der errado, voltar daqui
                bg_names = ['Level1Bg0', 'Level1Bg2', 'Level1Bg3']
                for copy in range(2):  # Duas Cópias para o Loop
                    for i, name in enumerate(bg_names):
                        y = (i + copy * len(bg_names)) * WIN_HEIGHT
                        list_bg.append(Background(name, (0, y)))
                return list_bg
