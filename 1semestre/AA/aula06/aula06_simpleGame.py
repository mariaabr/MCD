import random

def rollDice():
    return random.randint(1, 6), random.randint(1, 6)

def checkWin(red, green):
    return red > green

def main():
    print("Dice game!")
    print("You pay 1 euro to roll two dice > one RED and one GREEN.")
    print("You win 2 euros if there are more eyes on red than on green die.")

    numGames = 100
    wins = 0

    for i in range (100):        
        red, green = rollDice()

        print(f"\nRed die: {red}")
        print(f"Green die: {green}")

        if checkWin(red, green):
            print("\nCongratulations! You won 2 euros!")
            wins += 1
        else:
            print("\nBetter luck next time!")

    winProb = wins/numGames * 100 # percent

    print(f"\nSimulation Results:")
    print(f"Total games played: {numGames}")
    print(f"Number of wins: {wins}")
    print(f"Approximate probability of winning: {winProb:.2f}%")

if __name__ == "__main__":
    main()