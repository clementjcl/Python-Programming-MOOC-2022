import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 480-robot.get_height()


clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            x = x - robot.get_width()/2
            y = y - robot.get_height()/2

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