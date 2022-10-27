import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rect = robot.get_rect()
x = 0
y = 480-robot.get_height()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # if position mouse is in robot.rect=
            mx, my = pygame.mouse.get_pos()
            if mx in range(x, x+robot.get_width()) and my in range(y, y+robot.get_height()):
                x = random.randint(0, 640-robot.get_width())
                y = random.randint(0, 480-robot.get_height())


        if event.type == pygame.QUIT:
            exit()

    x = max(x,0)
    x = min(x,640-robot.get_width())
    y = max(y,0)
    y = min(y,480-robot.get_height())
    
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)