import random
player_wins = 0
computer_wins = 0
winning_game = 4

while player_wins < winning_game and computer_wins < winning_game:
    print(f"Score: Player: {player_wins} Computer: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")
    player = input("Make your move!").lower()
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

    if computer == player:
        print("Draw!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins.")
            computer_wins += 1
        elif computer == "scissors":
            print("Player wins.")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player wins.")
            player_wins += 1
        elif computer == "scissors":
            print("Computer wins.")
            computer_wins += 1
    elif player == "scissors":
        if computer == "rock":
            print("Computer wins.")
            computer_wins += 1
        if computer == "paper":
            print("Player wins")
            player_wins += 1
    else:
        print("Make a valid move")

if player_wins > computer_wins:
    print("Player wins the game!")
elif computer_wins > player_wins:
    print("Computer wins the game!")
else:
    print("The game ended in a tie")

print(f"Final Score: Computer:{computer_wins} Player: {player_wins}")