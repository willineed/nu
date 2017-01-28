1.
# Der mangler en parentes. Der skal stå temperature = float(input("Temperature: ")).
2.
# Program der viser om et tal er positiv, negativ eller lig 0.
tal = float(input("Indtast tal: "))

if tal > 0:
    print("Tallet er positivt")
elif tal == 0:
    print("Tallet er lig 0")
else:
    print("Tallet er negativt")
3.
# Hvis tallet er større end -10 og mindre eller lig med 10 printer den Succes.
user_input = float(input("Input a number: "))
if -10 < user_input <= 10:
    print("Succes")
else:
    print("Failure")
4.
# Ifølge programmet er A det eneste rigtige svar, men i virkeligheden er B også et rigtigt svar.
# Enten skal programmøren ændre svar mulighed B til noget andet
# Eller også skal han/hun skrive koden
# if user_input.upper() == "A" or user_input.upper() == "B":
# Så ville programmet være rigtigt.
5.
# Der skal ikke være dobbelt = tegn
# x >= 0: gør at hvis x er større eller lig 0 vil den skrive x is positive.
# Det vil vi ikke have, da x ikke er positivt hvis det er lig 0.
# Jeg har også ændret x = 4 til x = float(input("Write a number: ")), da man så selv kan skrive numre ind
# Udenfor programmet. Det er ikke som sådan en fejl, men hvis det er meningen at brugeren skal kunne
# skrive et tal ind er det vigtigt.

x = float(input("Write a number: "))
if x > 0:
    print("x is positive.")
else:
    print("x is not positive")
6.
# Man skal i stedet for skrive x = float(input("Enter a number: "))
# Brugeren kan skrive hvad som helst, hvis der ikke står float foran
# Hvis man vil skrive x lig med 3 skal der stå ==, da man ikke vil have tildelt x lig 3 i forvejen.
# Der skal være et : efter if statement.
7.
# Der skal stå if answer == "Beaker:
# Det er meget vigtigt at variablen har det samme navn
# der skal stå ==, da den kun må printe Correct ud hvis svaret er lig med Beaker
# else skal må ikke stå indrykket og der skal : bagpå
8.
# Der skal også stå x == "Glad": efter or.
9.
# Jeg vil formentlig gætte at der vil stå noget i retning af:
# x=5
# z=5
# Buzz

# Det mener jeg at det vil gøre, da y kun printes hvis x er lig med 6
# z derimod kan godt printes, da x er lig med 5
# print("x=", x) vil altid printe, da x allerede er defineret.
# derimod vil print("y=", y) ikke printe, da y kun er defineret hvis x er lig 6
# print("z=", z) printes, da z er lig 5
# hvis y er defineret printes der Fizz ud, men det er ikke tilfældet her
# Dog er z defineret og vil derfor printe Buzz ud

x = 5
y = x == 6
z = x == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print("Fizz")
if z:
    print("Buzz")

# Jeg gik ud fra at den ville printe det ud som jeg har skrevet tidligere, men det var ikke tilfældet.
# Den vil som jeg også sagde printe x=5 ud, dog printes der false ud ved y og true ud ved z
# Det er åbenbart fordi at den kun kigger på om statements'ne er falske eller sande
# og så printes der kun Buzz ud, da y er false.
10.
# jeg skriver det i rækkefølge efter 3, tallene er bare så du nemmere kan se hvilken linje jeg taler om.
# 4 True
# 5 False
# 6 True
# 7 False
# 8 False
# 9 True
# 10 False
# 11 False
# 12 True
# 13 False
# 14 True
11.
# True
# False
# True
# True
# True
# True
# False
# True
# False

12.
# Nu har jeg rettet i koden.
print("Welcome to Oregon Trail!")

print("A. Banker")
print("B. Carpenter")
print("C. Farmer")

user_input = input("What is your occupation? ")

if user_input == "A":
    money = 100
elif user_input == "B":
    money = 70
elif user_input == "C":
    money = 50

print("Great! you will start the game with", money, "dollars.")

