import random

comp_num = random.randint(1,10)
num = None

while num != comp_num:
    num = input("Guess a number between 1 and 10: ")
    num = int(num)
    if num == comp_num:
        print("That's right, you win.")
    elif num < comp_num:
        print("Too low, guess again")
    else:
        print("Too high, guess again.")

print(comp_num)


