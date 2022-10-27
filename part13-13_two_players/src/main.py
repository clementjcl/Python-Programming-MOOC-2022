import pygame

class Robot:
    def __init__(self, unit: int, x: int, y: int):
        self.unit = unit
        self.x = x
        self.y = y
        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False
    


pygame.init()
width, height = (640, 480)
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robots = []
units = 2

robot1 = Robot(1, 0, height-robot.get_height())
robot2 = Robot(2, width-robot.get_width(), height-robot.get_height())

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                robot1.to_left = True
            if event.key == pygame.K_RIGHT:
                robot1.to_right = True
            if event.key == pygame.K_UP:
                robot1.to_up = True
            if event.key == pygame.K_DOWN:
                robot1.to_down = True
                
            if event.key == pygame.K_a:
                robot2.to_left = True
            if event.key == pygame.K_d:
                robot2.to_right = True
            if event.key == pygame.K_w:
                robot2.to_up = True
            if event.key == pygame.K_s:
                robot2.to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                robot1.to_left = False
            if event.key == pygame.K_RIGHT:
                robot1.to_right = False
            if event.key == pygame.K_UP:
                robot1.to_up = False
            if event.key == pygame.K_DOWN:
                robot1.to_down = False

            if event.key == pygame.K_a:
                robot2.to_left = False
            if event.key == pygame.K_d:
                robot2.to_right = False
            if event.key == pygame.K_w:
                robot2.to_up = False
            if event.key == pygame.K_s:
                robot2.to_down = False


        if event.type == pygame.QUIT:
            exit()

    if robot1.to_right:
        robot1.x += 20
    if robot1.to_left:
        robot1.x -= 20
    if robot1.to_up:
        robot1.y -= 20
    if robot1.to_down:
        robot1.y += 20
        
    if robot2.to_right:
        robot2.x += 20
    if robot2.to_left:
        robot2.x -= 20
    if robot2.to_up:
        robot2.y -= 20
    if robot2.to_down:
        robot2.y += 20
    
    robot1.x = max(robot1.x,0)
    robot1.x = min(robot1.x,width-robot.get_width())
    robot1.y = max(robot1.y,0)
    robot1.y = min(robot1.y,height-robot.get_height())
    
    robot2.x = max(robot2.x,0)
    robot2.x = min(robot2.x,width-robot.get_width())
    robot2.y = max(robot2.y,0)
    robot2.y = min(robot2.y,height-robot.get_height())
    
    window.fill((0, 0, 0))
    window.blit(robot, (robot1.x, robot1.y))
    window.blit(robot, (robot2.x, robot2.y))
    pygame.display.flip()

    clock.tick(60)