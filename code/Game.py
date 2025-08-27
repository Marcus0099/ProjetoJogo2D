#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import sys

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu
from code.GameOver import GameOver


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
                if level_return == 'game over':
                    game_over_screen = GameOver(self.window)
                    game_over_screen.run()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()
