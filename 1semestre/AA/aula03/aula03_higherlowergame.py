# game to guess the chosen number between [1, 100]

import random

def randomNumber():
    number = random.randrange(1, 101)

    print("Chosen number:", number)
    return number

def guessNumber(higher, lower):
    number = random.randrange(lower, higher)

    # print("guess number:", number)
    return number

def game():
    
    # generate random integer
    number = randomNumber()

    # variables
    lower = 1
    higher = 101
    count = 1

    print("Guess a number: ", end="")
    guess = guessNumber(higher, lower)
    print(guess)

    while guess != number: # if didn't guess you continue playing

        # compare the guess
        if guess < number:
            print("lower")
            lower = guess + 1
            
        else:
            print("higher")
            higher = guess

        print("try again: ", end="")
        guess = guessNumber(higher,lower)
        print(guess)

        count += 1 # count the number of attempts

    print("You guessed! Congrats.") # guessed

    return count

def main():
    dict = {} # stores the number of games taht finished at x attempts and their percentage
    numberGames = 100000
    
    for i in range(numberGames):
        attempts = game()
        print("Number of attempts for game", i+1, ":", attempts, "\n")

        if attempts in dict:
            dict[attempts] += 1
        else:
            dict[attempts] = 1
    
    totalPercentage = 0

    for k,v in dict.items():
        # print(k,v)
        percent = v/numberGames * 100
        # print(percent, "%")

        dict[k] = (v, percent)
        totalPercentage += percent

    print("Total percentage:", totalPercentage, "% \n")

    # print(dict)

    for key, value in sorted(dict.items()):
        # print(key, value)

        print(key, "attempts:", dict[key][0], "-", dict[key][1],"%")


    keys = dict.keys()
    sortedkeys = sorted(list(dict.keys()))

    minAttempt = min(keys)
    print("MIN - The smallest number of attempts =", minAttempt)

    if len(sortedkeys) % 2 == 1: # if odd the middle number
        medianAttempt = sortedkeys[len(sortedkeys) // 2]
    else: # if even the average of the 2 central numbers
        medianAttempt = (sortedkeys[len(sortedkeys) // 2 - 1] + sortedkeys[len(sortedkeys) // 2]) / 2

    print("MEDIAN - The 'middle' number of attempts =", medianAttempt)

    mean = sum(keys)/len(keys)
    print("MEAN - The average number of attempts =", mean)

    maxAttempt = max(keys)
    print("MAX - The largest number of attempts =", maxAttempt)

main()