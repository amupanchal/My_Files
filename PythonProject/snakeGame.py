import random
def game_Win(comp, you):
    if comp == you:
        return  None
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer turn : choose Snake(s), Water(s)and Gun(3) ?")
randNo = random.randint(1, 3)

if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your turn : choose Snake(s) Water(w) and Gun(g) ?")
a = game_Win(comp, you)

print(f"Computer choose {comp}")
print(f"You choose {you}")

if a == None:
    print("Game is tie!! ")
elif a :
    print("You win!")
else:
    print("You Lose!!")
