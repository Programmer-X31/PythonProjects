import random
import time
import sys

wins = 0
losses = 0
ties = 0

while wins <= 10 or losses <= 10:
    if wins == 10:
        print("User won the tournament")
        sys.exit()
    elif losses == 10:
        print("AI won the tournament")
        sys.exit()

    choices = ["Rock", "Paper", "Scissor"]
    AIChoice = choices[random.randint(0, 2)]

    userChoice = str(
        input('Enter "Rock" for rock, "Scissor" for scissors or "Paper" for paper \n')
    )
    print("You chose " + userChoice)
    time.sleep(0.25)
    print("The AI chose " + AIChoice)

    if (
        (userChoice == "Rock" and AIChoice == "Scissor")
        or (userChoice == "Scissor" and AIChoice == "Paper")
        or (userChoice == "Paper" and AIChoice == "Rock")
    ):
        print("User Won!")
        wins = wins + 1
        print("%s Wins, %s Losses, %s Ties \n" % (wins, losses, ties))
    elif (
        (userChoice == "Scissor" and AIChoice == "Rock")
        or (userChoice == "Paper" and AIChoice == "Scissor")
        or (userChoice == "Rock" and AIChoice == "Paper")
    ):
        print("AI Won!")
        losses = losses + 1
        print("%s Wins, %s Losses, %s Ties \n" % (wins, losses, ties))
    else:
        print("It is a Tie!")
        ties = ties + 1
        print("%s Wins, %s Losses, %s Ties \n" % (wins, losses, ties))
