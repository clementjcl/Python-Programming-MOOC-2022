import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0, 0, 0))

rob_width = robot.get_width()
rob_height = robot.get_height()

width = 0
for i in range(0, 10):
    width += rob_width    
    window.blit(robot, (width, rob_height))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()