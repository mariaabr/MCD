import random

def rollDice():
    return random.randint(1, 6), random.randint(1, 6)

def checkWin(guess, sum):
    return guess == sum

def main():
    print("Dice game!")
    print("You pay 1 euro to roll two dice > guess the sum of eyes for the two dice")
    print("You win n euros if you can the guess the right sum of the dice eyes")

    numGames = 100
    wins = 0

    for i in range (100):        
        red, green = rollDice()
        sum = red + green

        print(f"\nRed die: {red}")
        print(f"Green die: {green}")
        print(f"Dice sum: {sum}")

        guess = random.randint(2, 12)
        print(f"\nGuess sum: {guess}")

        if checkWin(guess, sum):
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