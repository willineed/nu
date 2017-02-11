import pygame
from math import pi

ORANGE = (240, 140, 10)
YELLOW = (252, 252, 71)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
 
pygame.init()

size = (1001, 1001)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Ski Lift")
 
done = False
 
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Tegner baggrunden
    screen.fill(BLUE)
    
    # Tegner en hvid skibakke
    pygame.draw.polygon(screen, WHITE, [[0, 200], [0, 1000], [1000, 1000]], 0)
    # Tegner skiliften
    pygame.draw.line(screen, BLACK,[0, 0], [1000,800], 5)
    for x_y in range(1, 951, 150):
        pygame.draw.arc(screen, BLACK, [20 + x_y,0 + (x_y*4/5), 50, 100], 3*pi/2, 2*pi, 8)
        pygame.draw.arc(screen, BLACK, [24 + x_y,110 + (x_y*4/5), 50, 100], pi/2, pi, 8)
        pygame.draw.line(screen, BLACK,[47.5 + x_y,100 +(x_y*4/5)], [47.5 + x_y,110 +(x_y*4/5)], 5)
        pygame.draw.line(screen, BLACK,[25 + x_y,160 +(x_y*4/5)], [38 + x_y,160 +(x_y*4/5)], 5)
        pygame.draw.line(screen, BLACK,[38 + x_y,160 +(x_y*4/5)], [38 + x_y,150 +(x_y*4/5)], 2)
        pygame.draw.line(screen, BLACK,[25 + x_y,150 +(x_y*4/5)], [38 + x_y,150 +(x_y*4/5)], 2)

        # Manden med skiene
        pygame.draw.line(screen, BLACK,[35 + x_y,146 +(x_y*4/5)], [35 + x_y,160 +(x_y*4/5)], 3)
        pygame.draw.line(screen, BLACK,[35 + x_y,160 +(x_y*4/5)], [42 + x_y,160 +(x_y*4/5)], 3)
        pygame.draw.line(screen, BLACK,[42 + x_y,160 +(x_y*4/5)], [42 + x_y,170 +(x_y*4/5)], 3)
        pygame.draw.line(screen, BLACK,[34 + x_y,165 +(x_y*4/5)], [55 + x_y,175 +(x_y*4/5)], 2)
        pygame.draw.circle(screen, BLACK,[36 + x_y, 141 +int(x_y*4/5)], 0, 0)
        pygame.draw.circle(screen, BLACK,[35 + x_y, 141 +int(x_y*4/5)], 5, 2)
        
    # Tegner en flot sol
    pygame.draw.circle(screen, YELLOW,[800, 100], 40, 0)
    pygame.draw.circle(screen, ORANGE,[800,100], 30, 0)

    
 
    # --- Drawing code should go here
 

    pygame.display.flip()
    
    clock.tick(60)
 

pygame.quit()
