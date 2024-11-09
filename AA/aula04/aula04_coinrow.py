# coin row problem - pick the maximum value of n coins
# without picking any adjacent coins
import random
import time

def coinRowRec(coins, n):

    if n == 0:
        return 0 # no coin chosen

    if n == 1:
        return coins[0]
    
    return max((coins[n-1] + coinRowRec(coins, n-2)), coinRowRec(coins, n-1))

def main():
    coins = []
    size = random.randint(1, 10)
    values = [1, 2, 5, 10, 20, 50, 100, 200]
    coins = [values[random.randint(0, 7)] for s in range(size+1)]
    # coins = [5, 1, 2, 10, 6, 2] # f(n) = 17 
    print("Coin Row Problem with recursion")
    print(f"Coins set: {coins}")
    print(f"{'n':<5}{'r Maximum value(n)':<30}{'time':<20}")
    seconds = time.time()
    r = coinRowRec(coins, size)
    print(f"{size:<5}{r:<30}{seconds:<20}")

main()