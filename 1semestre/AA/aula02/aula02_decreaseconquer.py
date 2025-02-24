# Task 3 - DECREASE AND CONQUER VS RECURSIVE FUNCTION
# decrease and conquer algorithm

def aExpBRecursive (a, b, count = 0):
    
    # base cases
    
    if b == 0:
        return 1, count

    if b == 1:
        return a, count

    half_exp, count = aExpBRecursive(a, b // 2, count)

    if b % 2 == 0:
        # even, a^b = (a^(b//2)) * (a^(b//2))
        count += 1 # half * half
        return half_exp * half_exp, count
    else:
        # odd, a^b = (a^(b//2)) * (a^(b//2)) * a
        count += 2  # half * half * a
        return half_exp * half_exp * a, count

def main():
    print("function aExpBRecursive: ")

    print(f"{'n':<5}{'r aExpBRecursive(n)':<20}{'multiplications':<20}")
    for i in range(1, 18):
        r, count = aExpBRecursive(2, i)
        print(f"{i:<5}{r:<20}{count:<20}")

main()

## CONCLUSIONS
# base cases >> b = 0, return 1 and b = 1, return a
# number of multiplications depends on the parity of b: if b is even, is necessary one multiplication and if b is odd, are necessary two multiplications
# > the problem is divided in half (halved) in each step
# > the problem is divided in subproblems
# > this method does O(log(b) multiplications
# formal analysis: complexity is O(log(b)), with b being the exponent
# > the decrease-and-conquer method divide the problem in half in every recursion call
# > which is more efficient than the brute-force method with complexity O(b)
# empirical analysis: the decrease-and-conquer method is more efficient than the brute-force method, speccialy for large values of b
# > the number of multiplications grows slowly, which means that, for biggers values of b, this method has a better performance
# > for b = 1024, this approach divides the number of multiplications for nearly log2(1024) = 10, instead of the 1023 multiplications of brute-force