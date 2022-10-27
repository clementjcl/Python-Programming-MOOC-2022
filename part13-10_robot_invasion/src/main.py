import pygame
import random

pygame.init()

width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

units = 10
speed = 5
print(random.choice([0,1]))
robots = []
for i in range(units):
    robots.append([random.choice(range(0, width - robot.get_width())), random.choice(range(-1000, 0)), random.choice([0, 1])])


clock = pygame.time.Clock()
print(robots)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    for i in range(units):
        if robots[i][1] + robot.get_height() < height:
            robots[i][1] += speed
        else:
            if robots[i][0] < -(robot.get_width()) or robots[i][0] > width:
                robots[i][0] = random.choice(range(0, width - robot.get_width()))
                robots[i][1] = random.choice(range(-1000, 10))
            elif robots[i][2] == 0:
                robots[i][0] += speed
            else:
                robots[i][0] -= speed

    
    window.fill((0, 0, 0))
    for i in range(units):
        window.blit(robot, (robots[i][0], robots[i][1]))
    pygame.display.flip()

    clock.tick(60)