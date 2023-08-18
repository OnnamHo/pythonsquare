import pygame
from pygame.locals import *
import math

# Initialize Pygame and create a window
pygame.init()
scnwidth = 800
scnheight = 600
screen = pygame.display.set_mode((scnwidth, scnheight))

# Define the properties of the squares
square1_pos = [500.0, 550.0]
square1_size = 50
square1_velocity = 0.0
square1_velocity2 = 0.0
square1_mass = 1

square2_pos = [100.0, 550.0]
square2_size = 50
square2_velocity =  1.0
square2_velocity2 = 0.0
square2_mass = 10

#momentum
square1_momen = square1_mass*square1_velocity
square2_momen = square2_mass*square2_velocity
totalmass = square1_mass + square2_mass
srtotalmass = math.sqrt(totalmass)
init_momen = square1_momen + square2_momen
init_kin = 1/2*(square1_mass * square1_velocity * square1_velocity) + 1/2*(square2_mass * square2_velocity * square2_velocity)

count = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Update square positions
    
    square1_pos[0] += square1_velocity
    square2_pos[0] += square2_velocity

    # Check for collisions
    if square1_pos[0] < 0 or square1_pos[0] > scnwidth - square1_size:
        square1_velocity *= -1
        count+=1
        print("count: " + str(count))
    if square1_pos[1] < 0 or square1_pos[1] > scnheight - square1_size:
        square1_velocity *= -1


    if square2_pos[0] < 0 or square2_pos[0] > scnwidth - square2_size:
        square2_velocity *= -1
    if square2_pos[1] < 0 or square2_pos[1] > scnheight - square2_size:
        square2_velocity *= -1

    # Check for collision between squares
    if (square1_pos[0] < square2_pos[0] + square2_size and
            square1_pos[0] + square1_size > square2_pos[0] and
            square1_pos[1] < square2_pos[1] + square2_size and
            square1_pos[1] + square1_size > square2_pos[1]):
        # Reverse the velocities of both squares on collision
        count += 1
        square1_momen = square1_mass*square1_velocity
        square2_momen = square2_mass*square2_velocity

        init_momen = square1_momen + square2_momen
        init_kin = 1/2*(square1_mass * square1_velocity * square1_velocity) + 1/2*(square2_mass * square2_velocity * square2_velocity)

        square1_velocity2 = (math.sqrt(((2*init_kin*square2_mass - init_momen*init_momen)/square1_mass)+(init_momen*init_momen/(totalmass))) + (init_momen/srtotalmass))/srtotalmass
        square2_velocity2 = (init_momen - square1_mass*square1_velocity2)/square2_mass

        square1_velocity = square1_velocity2
        square2_velocity = square2_velocity2

        #square1_velocity *= -1
        #square2_velocity *= -1

        print("sq1 vel: " + str(square1_velocity))
        print("sq2 vel: " + str(square2_velocity))
        print("init momen: " + str(init_momen))
        print("init kin: " + str(init_kin))
        print("count: " + str(count))

    # Draw squares on the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (square1_pos[0], square1_pos[1], square1_size, square1_size))
    pygame.draw.rect(screen, (0, 0, 255), (square2_pos[0], square2_pos[1], square2_size, square2_size))
    pygame.display.update()

pygame.quit()