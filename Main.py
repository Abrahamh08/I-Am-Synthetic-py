import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            break
    else:
        pygame.display.flip()
        clock.tick(60)
        continue
    break