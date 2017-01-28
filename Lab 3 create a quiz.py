print("Velkommen til dansker quizzen!\nQuizzen består af fem spørgsmål.\nHvis du svarer alle rigtigt er du en rigtig dansker :).")
antal_rigtige = 0

# Hvad er hovedstaden i Danmark?

question_1 = input("\nHvad er hovedstaden i Danmark? ")
if question_1.lower() == "københavn":
    print("Korrekt!")
    antal_rigtige += 1
else:
    print("Forkert!")

# Hvad hedder vores dronning til fornavn?

question_2 = input("\nHvad hedder Danmarks dronning til fornavn? ")
if question_2.lower() == "margrethe":
    print("Korrekt!")
    antal_rigtige += 1
else:
    print("Forkert!")

# Hvad er den næststørste by i Danmark?

print("\nHvad er den næststørste by i Danmark?")
print("\nA. Odense")
print("B. Aalborg")
print("C. Aarhus")

question_3 = input("Svar: ")

if question_3.lower() == "c":
    print("Korrekt!")
    antal_rigtige += 1
else:
    print("Forkert!")

# Hvad hedder kronprinsen?
question_4 = input("\nHvad hedder Danmarks kronprins til fornavn? ")
if question_4.lower() == "frederik":
    print("Korrekt!")
    antal_rigtige += 1
else:
    print("Forkert!")


# matematik
question_5 = int(input("\nOg til sidst lidt matematik!\nHvad er 2+25*4-8/4? "))
if question_5 == 100:
    print("Korrekt!")
    antal_rigtige += 1
else:
    print("Forkert!")


print("\nDu har", antal_rigtige,"svar rigtige!")

procent_rigtige = antal_rigtige/5*100
print("Du har svaret", procent_rigtige,"% af spørgsmålene rigtigt!")
if procent_rigtige == 100:
    print("Du er en rigtig dansker!")
elif 70 < procent_rigtige < 100:
    print("Du er næsten en dansker!")
else:
    print("Der er lang vej til, at du er en rigtig dansker!")
    
