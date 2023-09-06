import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Set up the square
square_size = 10
square_pos = [size[0] // 2 - square_size, size[1] // 2 - square_size]
randsquare = [random.randrange(0, 400, 10), random.randrange(0, 400, 10), 10, 10]


# Set up the clock
clock = pygame.time.Clock()

#set up fall speed
speed = 1
movedir = 0

#list of square 
squarelist = []

def leftedgecoll():
    for allsquare in squarelist:
        #print(allsquare[1])
        if (square_pos[1] >= allsquare[1] and square_pos[1] < allsquare[1]+allsquare[3] and square_pos[0] + square_size == allsquare[0] or square_pos[1]+square_size > allsquare[1] and square_pos[1]+square_size <= allsquare[1]+allsquare[3] and square_pos[0] + square_size == allsquare[0]):
            return True
#        if (square_pos[0]+square_size == allsquare[0] and square_pos[1] >= allsquare[1] and square_pos[1] <= allsquare[1]+allsquare[3]):
#            return True
    return False

def rightedgecoll():
    for allsquare in squarelist:
        if (square_pos[1] >= allsquare[1] and square_pos[1] < allsquare[1]+allsquare[3] and square_pos[0] == allsquare[0] + allsquare[2] or square_pos[1]+square_size > allsquare[1] and square_pos[1]+square_size <= allsquare[1]+allsquare[3] and square_pos[0]  == allsquare[0] + allsquare[2]):
            return True
    return False

def topedgecoll():
    for allsquare in squarelist:
        if (square_pos[0] >= allsquare[0] and square_pos[0] < allsquare[0]+allsquare[2] and square_pos[1] + square_size == allsquare[1] or square_pos[0]+square_size > allsquare[0] and square_pos[0]+square_size <= allsquare[0]+allsquare[2] and square_pos[1] + square_size == allsquare[1]):
            return True
    return False 

def botedgecoll():
    for allsquare in squarelist:
        if (square_pos[0] >= allsquare[0] and square_pos[0] < allsquare[0]+allsquare[2] and square_pos[1] == allsquare[1] + allsquare[3] or square_pos[0]+square_size > allsquare[0] and square_pos[0]+square_size <= allsquare[0]+allsquare[2] and square_pos[1]  == allsquare[1] + allsquare[3]):
            return True       
    return False 

def canmoveleft():
    if (square_pos[0]-10 >= 0 and rightedgecoll()==False):
        return True

def canmoveright():
    if (square_pos[0]+square_size < size[0] and leftedgecoll()==False):
        return True

def canmoveup():
    if (square_pos[1]-10 >= 0 and botedgecoll() == False):
        return True

def canmovedown():
    if (square_pos[1]+square_size <= size[1] and topedgecoll() == False):
        return True

def reachleft():
    if square_pos[0] <= 0:
        square_pos[0] = 0

def reachright():
    if square_pos[0] >= size[0]:
        square_pos[0] = size[0]

def reachbottom():
    if square_pos[1]+square_size > size[1]:
        square_pos[1] = size[1]-square_size

def reachtop():
    if square_pos[1] <= 0:
        square_pos[1] = 0

#def swifttoleft():
#    if square_pos[0]+square_size >= size[0]:
#        square_pos[0] = 0

def endgame():
    #reach top
    if square_pos[1] <= 0:
        return True
    #reach left
    if square_pos[0]<= 0:
        return True
    #reach right
    if square_pos[0]+square_size >= size[0]:
        return True
    #reach bottom
    if square_pos[1] + square_size >= size[1]:
        return True
    return False

# Main game loop
while True:
    if endgame():
    #   break 
        #print("it reached") 
        print(square_pos[0], square_pos[1])

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if canmoveup():
                    movedir = 0
                    #square_pos[1] -= 10
                print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_DOWN:
                if canmovedown():
                    movedir = 1
                    #square_pos[1] += 10
                print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_LEFT:
                if canmoveleft():
                    movedir = 2
                    #square_pos[0] -= 10
                print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_RIGHT:
                if canmoveright():
                    movedir = 3
                    #square_pos[0] += 10
                print(square_pos[0], square_pos[1])

        
    #continuity
    if canmoveup() and movedir == 0:
        square_pos[1] -= speed
    if canmovedown() and movedir == 1:
        square_pos[1] += speed
    if canmoveleft() and movedir == 2:
        square_pos[0] -= speed
    if canmoveright() and movedir == 3:
        square_pos[0] += speed
    

    #logic check area
    reachleft()
    reachright()   
    reachtop()
    reachbottom()


    #collided
    if leftedgecoll() or rightedgecoll() or topedgecoll() or botedgecoll():
        squarelist.clear()
        #speed += 0.4
        randsquare = [random.randrange(0, 400, 10), random.randrange(0, 400, 10), 10, 10]


    # Update the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (square_pos[0], square_pos[1], square_size, square_size))
    pygame.draw.rect(screen, (255, 0, 0), (randsquare[0], randsquare[1], randsquare[2], randsquare[3]))
    squarelist.append(randsquare)
    

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)