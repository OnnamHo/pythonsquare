import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
size = (400, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Movable Square")

# Set up the square
square_size = 40
square_pos = [size[0] // 2 - square_size // 2, size[1] // 2 - square_size // 2]


occupied_squares = set()
# When a square is occupied, add its position to the set
occupied_squares.add((10, 10))

# Set up the clock
clock = pygame.time.Clock()

#set up fall speed
fallspeed = 1

def canmoveleft():
    if square_pos[0]-10 >= 0:
        return True

def canmoveright():
    if square_pos[0]+square_size < size[0]:
        return True

def canmoveup():
    if square_pos[1]-10 >= 0:
        return True

def canmovedown():
    if square_pos[1]+square_size <= size[1]:
        return True

def reachbottom():
    if square_pos[1]+square_size > size[1]:
        square_pos[1] = size[1]-square_size

def swifttoleft():
    if square_pos[0]+square_size >= size[0]:
        square_pos[0] = 0


# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            fallspeed = 0
            if event.key == pygame.K_UP:
                if canmoveup():
                    #if (square_pos[0], square_pos[1]) in occupied_squares == True:
                        square_pos[1] -= 10
                print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_DOWN:
                if canmovedown():
                    square_pos[1] += 10
                print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_LEFT:
                if canmoveleft():
                    square_pos[0] -= 10
                print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_RIGHT:
                if canmoveright():
                    square_pos[0] += 10
                print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_SPACE:
                if canmoveup():
                    square_pos[1] -= 30
        
    #continuity
    if canmovedown():
        square_pos[1]+=fallspeed
    if canmoveright():
        square_pos[0]+=1
    

    #logic check area
    fallspeed = fallspeed + 0.0981
    swifttoleft()    
    reachbottom()




    # Update the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (square_pos[0], square_pos[1], square_size, square_size))
    pygame.draw.rect(screen, (0, 255, 0), (0, 0, 20, 20))

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)