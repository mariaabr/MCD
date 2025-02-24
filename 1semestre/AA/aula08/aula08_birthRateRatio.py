import random

def monteCarloBirthRate ():

    domain = ['b'] * 51 + ['g'] * 49
    count = 0
    
    x = random.choice(domain) # first sample
    y = random.choice(domain) # second sample

    # print(x, y)

    if x == 'g' and y == 'g':   
        count += 1

    # print(count)

    return count

def main():
    
    result = 0
    samples = 10000

    for i in range (samples):
        result += monteCarloBirthRate()

    print("Result: ", result / samples)

if __name__ == "__main__":
    main()