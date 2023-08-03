import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
size = (100, 100)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Movable Square")

# Set up the square
square_size = 40
square_pos = [size[0] // 2 - square_size // 2, size[1] // 2 - square_size // 2]

# Set up the clock
clock = pygame.time.Clock()

def canmoveleft():
    if square_pos[0] > 0:
        return True

def canmoveright():
    if square_pos[0]+square_size < size[0]:
        return True

def canmoveup():
    if square_pos[1] > 0:
        return True

def canmovedown():
    if square_pos[1]+square_size < size[1]:
        return True

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if canmoveup() == True:
                    square_pos[1] -= 10
            elif event.key == pygame.K_DOWN:
                if canmovedown() == True:
                    square_pos[1] += 10
            elif event.key == pygame.K_LEFT:
                if canmoveleft() == True:
                    square_pos[0] -= 10
            elif event.key == pygame.K_RIGHT:
                if canmoveright() == True:
                    square_pos[0] += 10


    # Update the screen
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (square_pos[0], square_pos[1], square_size, square_size))

    # Flip the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
