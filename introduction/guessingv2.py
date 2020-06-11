import random
comp_num = random.randint(1, 10)
    num = None

while True:
    num = input("Guess a number between 1 and 10: ")
    num = int(num)
    if num > comp_num:
        print("Too high, guess again.")
    elif num < comp_num:
        print("Too low, guess again")
    else:
        print("YOU WON!!!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            comp_num = random.randint(1,10)
            num = None
        else:
            print("Thank you for playing!")
            break

print(comp_num)