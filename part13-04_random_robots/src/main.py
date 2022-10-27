import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

rob_width = robot.get_width()
rob_height = robot.get_height()

for i in range(1000):
        window.blit(robot, (random.choice(range(640-rob_width)), random.choice(range(480-rob_height))))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()