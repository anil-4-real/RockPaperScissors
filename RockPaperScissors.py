import random

def play():
    items = ["rock", "paper", "scissors"]
    counter = 0
    compScore = 0
    playerScore = 0
    tieCount = 0

    while True:
        comp = random.choice(items)
        playerInput = input("\nEnter your choice Rock, Paper, Scissors or Enter Q to quit: ").lower()

        if playerInput == "q":
            if compScore == 0 and playerScore == 0:
                print("\n\t| You played 0 times! |")
            else:
                print(F"\n\t| You won {playerScore} out of {counter} rounds! |")
                if tieCount > 0:
                    print(F"\t|    {tieCount} round(s) were tie!    |\n")
                    quit()

        if playerInput == comp:
            tieCount += 1
            print ("It's a tie!")

        elif playerInput == "rock":
            if comp == "paper":
                compScore += 1
                counter += 1
                print(F"You lose, the computer picked {comp}")
            elif comp == "scissors":
                playerScore += 1
                counter += 1
                print(F"You win!")

        elif playerInput == "paper":
            if comp == "scissors":
                compScore += 1
                counter += 1
                print(F"You lose, the computer picked {comp}")
            elif comp == "rock":
                playerScore += 1
                counter += 1
                print(F"You win!")

        elif playerInput == "scissors":
            if comp == "rock":
                compScore += 1
                counter += 1
                print(F"You lose, the computer picked {comp}")
            elif comp == "paper":
                playerScore += 1
                counter += 1
                print(F"You win!")


        else:
            print("Please enter valid option only")
            continue

play()
