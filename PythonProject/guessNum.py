import random
randNum = random.randint(1, 100)
print(randNum)

user = None
guess = 0

while (user != randNum):
    user = int(input("Enter a Number: "))
    if(user == randNum):
        print("Your guess is right !!")
    elif(user >= randNum):
        print("Choose Less Number than random number")
    elif (user <= randNum):
        print("Choose greater Number than random number")
    else:
        if (user > randNum):
            print("Your guess is wrong!! Enter Less Number")
        else:
            print("Your guess is wrong!! Enter greater Number")

        print("Your guess is wrong!!")
    guess +=1


print(f"Your guess the number in {guess} guess")
