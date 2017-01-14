1.
print("William Abildtrup")
2.
#det her er en kommentar
3.
# Den første giver 0,666666...
# Den anden derimod runder tallet ned til det nærmeste hele tal,
# da der er to divisionstegn og giver derfor 0.
print(2/3)
print(2 // 3)
4.
pi = 3.14
print(pi)
5.
# Programmering er meget sensitiv til valget af store og små bogstaver osv.
# Det er derfor vigtigt at du skriver det på præcist den samme måde.
A = 22
print(A)
6.
# area_of_rectangle ville være det bedre brugte navn,
# da det siger noget om hvilken variabel det er.
7.
# 1Apple virker ikke da der er tal foran ordet.
# account number virker ikke da der er mellemrum.
# account.number virker ikke da der er punktum.
# account# virker som sådan ikke hvis du vil skrive kode bagefter. Programmet behandler det som en kommentar.
# great.big.variable virker ikke da der er punktum.
# 2x virker ikke da der er tal foran
# #left dur ikke hvis du vil skrive kode bagefter. Programmet behandler det som en kommentar.

8.
# Koden kigger kun på tal ovenover og aldrig nedenunder.
9.
# Der er ingen grund til at man bruger input eller float, da pi er en konstant.
# Hvis man dog absolut vil inputte pi til at være 3.14 kan man lave en kode
pi = input("Enter the value of pi:")
pi = float(pi)
10.
# Koden er mere kompliceret og længere end den burde være og kan ændres til:

radius = float(input("Radius:"))
area = 3.14 * radius ** 2
print(area)
# Jeg har fjernet pi = 3.14, da pi alligevel er en konstant.
11.
# Der skal ikke være parentes rundt om x og y hver for sig. Eller i det hele taget.
x = 4
y = 5
a = x * y
print(a)
12.
# Alle tegnene skal skrives
a = 3 * (x + y)
print(a)
13.
# Float skal bytte plads med input.
14.
# De printer alle sammen det samme ud.
# Dog ville nr. 2 være den mest korrekte måde at skrive det på i programmering.
15.
# En konstant er et nummer der aldrig ændrer sig
16.
# Navnet skrives i capslock. Dvs. alle bogstaverne er store.
17.
# single quote: '. double quote: "
18.
print("Jeg skriver nu et python program, der laver en \" og en ny linje.\r\nDen nye linje er her!")
19.
print('Det kan det godt')
20.
# Der skal være parentes rundt om 3+4+5, da python ser det som 5/3.
print((3 + 4 + 5) / 3)
21.
# En operator er et symbol som + eller -.
22.
# Det printer tallet 3 ud, da der ikke står x = x + 1 i linje 2.
x = 3
x + 1
print(x)
23.
user_name = input("Enter your name: ")
24.
user_age = float(input("Enter your age: "))
