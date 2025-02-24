# Task 1 - DIRECT ALGORITHM ITERATIVE VS RECURSIVE
# brute force algorithm

def aExpB (a, b):

    result = 1
    count = 0 # count the number of multiplications

    if b == 0:
        return result, count

    if b == 1:
        return a, count

    for i in range(b):
        result *= a
        count += 1

    return result, count-1 # always enter in the loop but the first multiplication doesn't count, just initialize the number a as we want

def aExpBRecursive (a, b, count=0):

    # base cases

    if b == 0:
        return 1, count
    
    if b == 1:
        return a, count
    
    count += 1
    result, count = aExpBRecursive(a, b-1, count)
    return a * result, count
    # return a * aExpBRecursive(a, b-1)
    
def main():
    print("Iterative function aExpB: ")

    print(f"{'n':<5}{'r aExpB(n)':<20}{'multiplications':<20}")
    for i in range(1, 11):
        r, count = aExpB(2, i)
        print(f"{i:<5}{r:<20}{count:<20}")

    print("Recursive function aExpBRecursive: ")
    
    print(f"{'n':<5}{'r aExpBRecursive(n)':<20}{'multiplications':<20}")
    for i in range(1, 11):
        r, count = aExpBRecursive(2, i)
        print(f"{i:<5}{r:<20}{count:<20}")

main()

# completar com numero de iterações e outros

## CONCLUSIONS
# base cases recursion >> b = 0, return 1 and b = 1, return a
# number of multiplications >> iterative b-1, recursion b-1
# formal analysis: iterative runs a loop b-1 times >> complexity O(b), with b being the exponent
#                  recursion makes b-1 calls >> complexity O(b), with b being the exponent
# empirical analysis: similar time complexity but the recursion approach incurs the overhead of multiple function calls and stack space usage
# > with a large value for b, the reucrion can result in a stack overflow
# > thus, in practice and for the brute-force algorithm, the iterative approach tends to be more efficient
# the recursion on the brute-force approach doesn't provide any performance gain, over iterative, because:
# > both methods performa the same number of multiplications (b-1)
# > recursion has extra overhead due to function calls and stack management