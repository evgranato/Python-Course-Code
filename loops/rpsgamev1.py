
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player 1, make your move:")
player2 = input("player 2, make your move:")

# rock beats scissors
# paper beats rock
# scissors beats paper
if player1 == "rock" and player2 == "scissors":
    print("Player 1 wins!")
elif player1 == "paper" and player2 == "rock":
    print("Player 1 wins!")
elif player1 =="scissors" and player2 == "paper":
    print("Player 1 wins!")
elif player2 == "rock" and player1 == "scissors":
    print("Player 2 wins!")
elif player2 == "paper" and player1 == "rock":
    print("Player 2 wins!")
elif player2 == "scissors" and player1 == "paper":
    print("Player 2 wins!")
elif player1 == player2:
    print("Draw")
else:
    print("Something went wrong")