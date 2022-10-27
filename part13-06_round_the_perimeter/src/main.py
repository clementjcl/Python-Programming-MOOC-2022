import pygame

pygame.init()


window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
direction = 1 # 1=right, 2=down, 3=left, 4=up

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if direction == 1:
        x += velocity
        if x + robot.get_width() >= window.get_width():
            direction = 2
            print("down")
    elif direction == 2:
        y += velocity
        if y + robot.get_height() >= window.get_height():
            direction = 3
            print("left")
    elif direction == 3:
        x -= velocity
        if x <= 0:
            direction = 4
            print("up")
    elif direction == 4:
        y -= velocity
        if y <= 0:
            direction = 1
            print("right")

    clock.tick(60)