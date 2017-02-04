import random
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your")
print("desert trek and outrun the natives.")

traveled = 0
miles_traveled = 0
thirst = 0
camel_tiredness = 0
natives_traveled = -20
drinks_canteen = 4
done = False

while not done:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full sped.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    user_choice = input("Your choice? ")
    if user_choice.upper() == "Q":
        done = True
    elif user_choice.upper() == "E":
        print("Miles traveled:", miles_traveled)
        print("Drinks in canteen:", drinks_canteen)
        print("The natives are", miles_traveled - natives_traveled,"miles behind you.")
        print("")
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("The camel is happy")
        print("")
        natives_traveled += random.randrange(7, 15)
    elif user_choice.upper() == "C":
        traveled = random.randrange(10, 21)
        print("You just traveled", traveled, "miles.")
        print("")
        miles_traveled += traveled
        thirst += 1
        camel_tiredness += random.randrange(1, 4)
        natives_traveled += random.randrange(7, 15)
    elif user_choice.upper() == "B":
        traveled = random.randrange(5, 13)
        print("You just traveled", traveled, "miles.")
        print("")
        miles_traveled += traveled
        thirst += 1
        camel_tiredness += 1
        natives_traveled += random.randrange(7, 15)
    elif user_choice.upper() == "A":
        if drinks_canteen > 0:
            thirst = 0
            drinks_canteen -= 1
            print("You have satiated your thirst")
            print("")
        else:
            print("You do not have any drinks left.")

    if random.randrange(1, 21) == 1:
        print("You have found an oasis!")
        print("Your canteen has been refilled.")
        print("Your thirst has been satiated.")
        print("Your camel is now rested.")
        drinks_canteen = 4
        thirst = 0
        camel_tiredness = 0
        print("")

    if thirst > 6:
        print("You died of thirst!")
        done = True
    elif thirst > 4:
        print("You are thirsty!")
        print("")

    if camel_tiredness > 8:
        print("Your camel is dead.")
        done = True
    elif camel_tiredness > 5:
        print("Your camel is getting tired.")
        print("")

    if natives_traveled >= miles_traveled:
        print("The natives have caught you!")
        done = True
    elif (miles_traveled - natives_traveled)< 15:
        print("The natives are getting close!")
        print("")

    if miles_traveled >= 200:
        print("You have made it across the desert!")
        print("You have succesfully outrun the natives!")
        done = True

    

    

