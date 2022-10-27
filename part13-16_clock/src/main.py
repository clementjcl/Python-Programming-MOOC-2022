import pygame
import math
from datetime import datetime


def hand(length: int, color, thick: int, angle: float):
    x = rect.centerx + length * math.sin(angle)
    y = rect.centery - length * math.cos(angle)

    pygame.draw.line(display, color, [rect.centerx, rect.centery], (x, y), thick)


pygame.init()

# Display setup and values
width, height = 640, 480
display = pygame.display.set_mode((width, height))
rect = display.get_rect()

# Define some colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Length clock hands
hand_second_len = 180
hand_minute_len = 170
hand_hour_len = 130


# Events
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                exit()
     
    # Display properties
    pygame.display.set_caption(str(datetime.now().time())[:8])
    display.fill((0, 0, 0)) 

    # Drawing circles
    pygame.draw.circle(display, red, (rect.centerx, rect.centery), 200, width=4)
    pygame.draw.circle(display, red, (rect.centerx, rect.centery), 10, width=0)

    # Getting time
    hours = datetime.now().hour % 12
    minutes = datetime.now().minute
    seconds = datetime.now().second
    
    # Daw seconds hand
    s_angle = seconds*2*math.pi/60
    hand(hand_second_len, blue, 1, s_angle)
    
    # Draw minutes hand
    m_angle = minutes*2*math.pi/60 + seconds*2*math.pi/(60*60)
    hand(hand_minute_len, green, 2, m_angle)

    # Draw hours hand
    h_angle = hours*2*math.pi/12 + minutes*2*math.pi/(12*60)
    hand(hand_hour_len, yellow, 5, h_angle)
    
    
    # Updating display
    pygame.display.flip()