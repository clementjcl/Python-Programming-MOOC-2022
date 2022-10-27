import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

x1 = 0
x2 = 0
velocity1 = 5
velocity2 = 10
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x1, robot.get_height()))
    window.blit(robot, (x2, robot.get_height()*2))
    pygame.display.flip()
    
    x1 += velocity1
    if x1 == 0 or x1+robot.get_width() == width:
        velocity1 = -velocity1
    x2 += velocity2
    if x2 == 0 or x2+robot.get_width() == width:
        velocity2 = -velocity2
    

    clock.tick(60)