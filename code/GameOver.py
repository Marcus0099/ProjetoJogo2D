import sys
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from code.Const import WIN_WIDTH, C_BLACK, C_WHITE


class GameOver:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        self.options = ('RETORNAR AO MENU', 'SAIR',)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/GameOver.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(80, "BATEU!", C_BLACK, ((WIN_WIDTH / 2), 70))

            for i in range(len(self.options)):
                if i == menu_option:
                    self.menu_text(25, self.options[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(25, self.options[i], C_BLACK, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(self.options) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(self.options) - 1
                    if event.key == pygame.K_RETURN:
                        if menu_option == 0:
                            return 'game_over'
                        elif menu_option == 1:
                            pygame.quit()
                            sys.exit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Console", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
