import random
player_wins = 0
computer_wins = 0
winning_score = 4

while player_wins < winning_score and computer_wins < winning_score:
# repeats it 3 times
# for time in range(3):
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    player = input("player, make your move:").lower()
    if player == "quit" or player == "q":
        break
    rand_num = random.randint(0,2)
    if (rand_num == 0):
        computer = "rock"
    elif (rand_num == 1):
        computer = "paper"
    else:
        computer = "scissors"
    print(f"Computer plays {computer}")

    if player == computer:
        print("Draw!")
    elif player == "rock":
        if computer == "scissors":
            print("Player wins!")
            player_wins += 1
        elif computer == "paper":
            print("computer wins!")
            computer_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins!")
            player_wins += 1
        elif computer == "scissors":
            print("computer wins!")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("computer wins!")
            computer_wins += 1
        elif computer == "paper":
            print("Player wins!")
            player_wins += 1
    else:
         print("Please enter a valid move.")
if player_wins > computer_wins:
    print("Congrats, you won!")
elif player_wins == computer_wins:
    print("It's a tie!")
else:
    print("Uh oh, the computer won.")

print(f"Final Score: Player:{player_wins} Computer:{computer_wins}")