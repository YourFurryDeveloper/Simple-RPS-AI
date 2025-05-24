import time
import random
import os

os.system("clear")

def game():
    rounds = int(input("Number of rounds: "))
    print("There are two AI players. \n")
    time.sleep(1)

    moves = ["rock", "paper", "scissors"]

    ai1wins = 0
    ai2wins = 0
    draws = 0

    for i in range(rounds):
        ai1moveNum = random.randint(0, 2)
        ai1move = moves[ai1moveNum]
        print("AI 1 chose " + ai1move)

        time.sleep(0)

        ai2moveNum = random.randint(0, 2)
        ai2move = moves[ai2moveNum]
        print("AI 2 chose " + ai2move)

        if ai1moveNum > ai2moveNum:
            print("AI 1 wins!")
            ai1wins += 1
        elif ai1moveNum < ai2moveNum:
            print("AI 2 wins!")
            ai2wins += 1
        else:
            print("Draw!")
            draws += 1

        print("")
        time.sleep(0)

    print("\n==========\n")
    print("AI 1 total wins: " + str(ai1wins))
    print("AI 2 total wins: " + str(ai2wins))
    print("Total draws: " + str(draws))
    print("")
    if ai1wins > ai2wins:
        print("Winner: AI 1 by " + str(ai1wins - ai2wins) + " rounds")
    else:
        print("Winner: AI 2 by " + str(ai2wins - ai1wins) + " rounds")

game()
