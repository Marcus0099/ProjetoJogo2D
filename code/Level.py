#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY1, EVENT_ENEMY2, WIN_WIDTH, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Enemy import Enemy


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1Car'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2Car'))
        pygame.time.set_timer(EVENT_ENEMY1, SPAWN_TIME['Enemy1Car'])
        pygame.time.set_timer(EVENT_ENEMY2, SPAWN_TIME['Enemy2Car'])

    def is_safe_spawn(self, new_rect):
        for ent in self.entity_list:
            if isinstance(ent, Enemy):
                if new_rect.colliderect(ent.rect):
                    return False
        return True

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY1:
                    for _ in range(10):
                        x = random.randint(0, WIN_WIDTH - 50)
                        y = -10
                        enemy = EntityFactory.get_entity('Enemy1Car')
                        enemy.rect.topleft = (x, y)
                        if self.is_safe_spawn(enemy.rect):
                            self.entity_list.append(enemy)
                            break
                if event.type == EVENT_ENEMY2:
                    for _ in range(10):
                        x = random.randint(0, WIN_WIDTH - 50)
                        y = -10
                        enemy = EntityFactory.get_entity('Enemy2Car')
                        enemy.rect.topleft = (x, y)
                        if self.is_safe_spawn(enemy.rect):
                            self.entity_list.append(enemy)
                            break

            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            # Collisions
            if EntityMediator.verify_collision(entity_list=self.entity_list):
                return 'game over'
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Console", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
