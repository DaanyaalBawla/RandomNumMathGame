import random
gamestart= input("Welcome to the RNG addition game! Press e to exit")
if gamestart.lower() == "e":
    exit()
else:
    gamestart = True

while gamestart:
    rannumb1 = random.randint(0, 500)
    rannumb2 = random.randint(0, 500)
    answer = input("Add these numbers " + str(rannumb1) + "+" + str(rannumb2))
    correctnum = rannumb1 + rannumb2
    if answer == str(correctnum) :
        print("That's correct!")
        break
    else:
        print("That is incorrect! Try again. The answer was: " + str(correctnum))
