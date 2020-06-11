# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("player, make your move:").lower()
import random
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("Player wins!")
    elif computer == "paper":
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("Player wins!")
    elif computer == "scissors":
        print("computer wins!")
elif player == "scissors":
    if computer == "rock":
        print("computer wins!")
    elif computer == "paper":
        print("Player wins!")
else:
     print("Please enter a valid move.")