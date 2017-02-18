import pygame
6.1
b = 10
for i in range(9):
    b += i
    for j in range(i+1):
        print (b+j,end=" ")
 
    print()


6.2
# Jeg har lige givet den en ekstra tweak, da programmet ikke vil fungere som det skal
# hvis integer-nummeret er 2 eller under.

print()

a = False
b = 0

while not a:
    user_input = int(input("Input a positive integer number above 2: "))
    if user_input <= 2:
        print("The integer number is not above 2")
        print()
    else:
        # Laver den første linje
        for i in range(1):
            for j in range(user_input*2):
                print(b, end= "")
            print()

        # Laver det i midten
        for i in range(user_input-2):
            for j in range(2):
                print(b, end= (user_input*2-2)*(" "))
            print()
            
        # Laver den sidste linje
        for i in range(1):
            for j in range(user_input*2):
                print(b, end= "")
            print()
        a = True

6.3

# jeg gav lidt op på denne her opgave, men den nederste del er næsten færdig.

user_input = int(input("Input a positive integer number: "))

# Nederste venstre trekant og højre trekant
c = 2*(user_input-1)+3
for i in range(user_input):
    c -= 2
    for j in range(0, i*2+2, 2):
        print(c+j, end=" ")
    for j in range(c-3-2*i):
        print(" ", end=" ")
    for j in range(i*2, -2, -2):
        print(c+j, end=" ")
                
    print()

6.4


BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.init()
 

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Green rectangles")
 

done = False
 

clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    screen.fill(BLACK)

    # Laver et gitter af grønne firkanter
    for i in range(1,800,8):  
        for j in range(1,800,8):
            pygame.draw.rect(screen,GREEN,[0+i,0+j,4,4],0)
    
 
    
    pygame.display.flip()
 
    
    clock.tick(60)
 
pygame.quit()

