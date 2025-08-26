# C
import pygame

C_RED = (255, 0, 0)
C_WHITE = (255, 255, 255)

# E
EVENT_ENEMY1 = pygame.USEREVENT + 1
EVENT_ENEMY2 = pygame.USEREVENT + 2


ENTITY_SPEED = {
    'Player1Car': 4,
    'Player2Car': 4,
    'Enemy1Car': 3,
    'Enemy2Car': 2,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Player1Car': 1,
    'Player2Car': 1,
    'Enemy1Car': 1,
    'Enemy2Car': 1,
}

# M
MENU_OPTION = ('NOVO JOGO 1P',
               'NOVO JOGO 2P',
               'SAIR',)

# W
WIN_WIDTH = 565
WIN_HEIGHT = 650

# P
PLAYER_KEY_UP = {'Player1Car': pygame.K_UP,
                 'Player2Car': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1Car': pygame.K_DOWN,
                    'Player2Car': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1Car': pygame.K_LEFT,
                 'Player2Car': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1Car': pygame.K_RIGHT,
                 'Player2Car': pygame.K_d}

# S
SPAWN_TIME = {'Enemy1Car': 3000,
              'Enemy2Car': 2000,}
