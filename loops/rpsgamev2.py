print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player 1, make your move:")
print("***No Cheating\n\n" *20)
# this line adds \n new line, double spaced, and 20 times
player2 = input("player 2, make your move:")

if player1 == player2:
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("Player 1 wins!")
    elif player2 == "paper":
        print("Player 2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("Player 1 wins!")
    elif player2 == "scissors":
        print("Player 2 wins!")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 wins!")
    elif player2 == "paper":
        print("Player 1 wins!")
else:
    print("Something went wrong.")
# if player 2 enters gibberish, you won't get the "something went wrong" because of the way the input is player1 dependent.

# v1 code
# rock beats scissors
# paper beats rock
# scissors beats paper
# if player1 == "rock" and player2 == "scissors":
#     print("Player 1 wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("Player 1 wins!")
# elif player1 =="scissors" and player2 == "paper":
#     print("Player 1 wins!")
# elif player2 == "rock" and player1 == "scissors":
#     print("Player 2 wins!")
# elif player2 == "paper" and player1 == "rock":
#     print("Player 2 wins!")
# elif player2 == "scissors" and player1 == "paper":
#     print("Player 2 wins!")
# elif player1 == player2:
#     print("Draw")
# else:
#     print("Something went wrong")