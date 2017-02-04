import random
1.
for i in range(10):
    print("William")
print("Done")
2.
for i in range(20):
    print("Red")
    print("Gold")
3.
for i in range(2,101,2):
    print(i)
4.
i = 10
while i > 0:
    i -= 1
    print(i)
print("Blast off!")
5.
# der skal enten stå float eller int foran input, da det skal være et tal man skriver.
# totalet skal plusses med x, da vi selv vil bestemme inputtet
# der skal printes total ud og ikke x ud.
# Vi får til sidst koden
# bemærk at jeg har valgt float, da jeg tillader decimaltal.
print("This program takes three numbers and returns the sum.")
total = 0
 
for i in range(3):
    x = float(input("Enter a number: "))
    total = total + x
print("The total is:", total)
6.
number = random.randrange(1, 11)
print(number)
7.
number = random.random() * 9 + 1
print(number)
8.
total_positive = 0
total_zero = 0
total_negative = 0
total = 0
for i in range(7):
    x = float(input("Enter a number: "))
    total = total + x
    if x > 0:
        total_positive += 1
    elif x == 0:
        total_zero += 1
    else:
        total_negative += 1
print("The total is:", total)
print("Total positive entries:", total_positive)
print("Total entries equal to zero:", total_zero)
print("Total negative entries:", total_negative)
9.
total_heads = 0
total_tails = 0
for i in range(50):
    number = random.randrange(2)
    if number == 0:
        print("Heads")
        total_heads += 1
    if number == 1:
        print("Tails")
        total_tails += 1
print("You have a total of:", total_heads,"heads.")
print("You have a total of:", total_tails,"tails.")
10.
# Jeg har givet rock, paper, scissors henholdsvist "fiktive" numre for deres value. rock=0, paper=1 og scissors=2
# Det gør det sværere for programmøren, men det giver et mere lækkert program.
print("Welcome to rock, paper and scissors!")
number = random.randrange(3)
user_input = input("What play do you choose? Rock, paper or scissors? ")
if user_input.lower() == "rock":
    if number == 0:
        print("The computer played rock.")
        print("It's a tie!")
    if number == 1:
        print("The computer played paper.")
        print("You've lost!")
    if number == 2:
        print("The computer played scissors.")
        print("You've won!")
        
if user_input.lower() == "paper":
    if number == 0:
        print("The computer played rock.")
        print("You've won!")
    if number == 1:
        print("The computer played paper.")
        print("It's a tie!")
    if number == 2:
        print("The computer played scissors.")
        print("You've lost!")
        
if user_input.lower() == "scissors":
    if number == 0:
        print("The computer played rock.")
        print("You've lost!")
    if number == 1:
        print("The computer played paper.")
        print("You've won!")
    if number == 2:
        print("The computer played scissors.")
        print("It's a tie!")

    
