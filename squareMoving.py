import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
size = (400, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Movable Square")

# Set up the square
square_size = 40
#square_pos = [size[0] // 2 - square_size // 2, size[1] // 2 - square_size // 2]
square_pos = [0,0]

square2 = [50, 80, 50, 200]
square3 = [100, 300, 50, 120]
square4 = [270, 450, 200, 30]


occupied_squares = set()
# When a square is occupied, add its position to the set
occupied_squares.add((10, 10))

# Set up the clock
clock = pygame.time.Clock()

#set up fall speed
fallspeed = 1

#list of square 
squarelist = []

#can only handle same size
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

def reachbottom():
    if square_pos[1]+square_size > size[1]:
        square_pos[1] = size[1]-square_size

def reachtop():
    if square_pos[1] <= 0:
        square_pos[1] = 0

def swifttoleft():
    if square_pos[0]+square_size >= size[0]:
        square_pos[0] = 0

def endgame():
    if square_pos[1] + square_size >= size[1]:
        return True




# Main game loop
while True:
    
    #if endgame():
    #   break 
        #print("it reached bottom") 

    # Handle events
    #if (square_pos[0] < square2_pos[0] + square_size and square_pos[0] + square_size > square2_pos[0] and square_pos[1] < square2_pos[1] + square_size and square_pos[1] + square_size > square2_pos[1]):
        #fallspeed = 0

    #if (leftedgecoll() or rightedgecoll() or topedgecoll() or botedgecoll()):
        #print("boom")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            fallspeed = 0
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.key == pygame.K_UP:
                if canmoveup():
                    square_pos[1] -= 30
                #print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_DOWN:
                if canmovedown():
                    square_pos[1] += 20
                #print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_LEFT:
                if (canmoveleft()):
                    square_pos[0] -= 20
                #print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_RIGHT:
                if canmoveright():
                    square_pos[0] += 20
                #print(square_pos[0], square_pos[1])
            elif event.key == pygame.K_SPACE:
                if canmoveup():
                    square_pos[1] = 0
        
    #continuity
    if canmovedown():
        square_pos[1]+=fallspeed
    if canmoveright():
        square_pos[0]+=1
    

    #logic check area
    #gravity
    fallspeed = 1
    swifttoleft()    
    reachtop()
    reachbottom()




    # Update the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (square_pos[0], square_pos[1], square_size, square_size))
    pygame.draw.rect(screen, (0, 255, 0), (square2[0], square2[1], square2[2], square2[3]))
    pygame.draw.rect(screen, (0, 0, 255), (square3[0], square3[1], square3[2], square3[3]))
    pygame.draw.rect(screen, (0, 130, 255), (square4[0], square4[1], square4[2], square4[3]))
    squarelist.append(square2)
    squarelist.append(square3)
    squarelist.append(square4)
    #print(squarelist[0][0])

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)





#----------------------------------------------------
#29/8/23
#current problem: when the moving square is smaller than the length of an edge, it will pass through since 
#the implementation of edge collision only applies to moving square's top and bottom pixel