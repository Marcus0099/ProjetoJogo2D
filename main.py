import pygame

pygame.init()
window = pygame.display.set_mode(size=(480, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
