import pygame
import random


pygame.init()

# Create clock to control speed of the animation
clock = pygame.time.Clock()

# Display Setup and background surface
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
display = screen.get_rect()
background = pygame.Surface((width, height))

# Load robot image and get its rect
robot_img = pygame.image.load("robot.png")
robot = robot_img.get_rect()

robot.centerx = display.centerx 
robot.bottom = display.bottom
robot_speed = 10


to_right = False
to_left = False

# Load rock image and properties
rock = pygame.image.load("rock.png")
units = 10
rock_speed = 1
# Create a list of Rocks / rock=(X position, Y position) / with Units = number rocks
rocks = []
for i in range(units):
    rocks.append([random.choice(range(0, width - rock.get_width())), random.choice(range(-1000, 0))])


# Create font for text and declare points
font = pygame.font.SysFont("Arial", 26)
points = 0

# Loop (executed 60 times per second according to clock.tip(argument))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                exit()
            elif event.key == pygame.K_RIGHT:
                to_right = True
            elif event.key == pygame.K_LEFT:
                to_left = True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                to_right = False
            elif event.key == pygame.K_LEFT:
                to_left = False
    
    
    # Update robot's position based on movement flags
    if to_right and robot.right < display.right:
        robot.centerx += robot_speed
    elif to_left and robot.left > 0:
        robot.centerx -= robot_speed
            
    # Update rock's position
    for i in range(units):
        # Check if rock rect is in contact with robot rec
        rocks[i][1] += rock_speed
        # Game Over!
        if rocks[i][1] + rock.get_height() >= display.bottom:
            exit()
        # Hit the Rock! +1 point
        if rocks[i][1] + rock.get_height() >= robot.top:
            rock_middle = rocks[i][0]+rock.get_width()/2
            if robot.centerx-rock_middle <= (robot_img.get_width()+rock.get_width())/2:
                rocks[i][0] = random.choice(range(0, width - rock.get_width()))
                rocks[i][1] = random.choice(range(-1000, 10))
                points += 1
                
    # Filling display with black color
    background.fill((0, 0, 0))
    
    # The robot is drawn at the given location
    background.blit(robot_img, (robot.left, robot.top))
    
    # The rocks are drawn at the given location
    for i in range(units):
        background.blit(rock, (rocks[i][0], rocks[i][1]))
    
    screen.blit(background, (0, 0))
    
    # The text is drawn
    text = font.render("Points: "+str(points), True, (255, 0, 0))
    screen.blit(text, (width-125, 10))

    pygame.display.flip()
    
    # Loop is executed 60 times a second (approximately matches the FPS or frames per second value used with games)
    clock.tick(60)