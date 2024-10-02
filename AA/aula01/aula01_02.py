# algoritmos recursivos

import time

def r1(n):
    if n == 0:
        return 0
    return 1 + r1(n-1)

def r2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n + r2(n-2)

def r3(n):
    if n == 0:
        return 0
    return 1 + 2*r3(n-1)

def r4(n):
    if n == 0:
        return 0
    return 1 + r4(n-1) + r4(n-1)

def measureExecutionTime(func, n): # calculates the execution time of a function with a n
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

def main():

    print("all results in one table:")
    print(f"{'n':<5}{'r r1(n)':<20}{'r r2(n)':<20}{'r r3(n)':<20}{'r r4(n)':<20}")
    for i in range(1, 11):
        print(f"{i:<5}{r1(i):<20}{r2(i):<20}{r3(i):<20}{r4(i):<20}")

    print() # tables break
    
    print("all results in one table - execution time:")
    print(f"{'n':<5}{'exec time r1(n)':<20}{'exec time r2(n)':<20}{'exec time r3(n)':<20}{'exec time r4(n)':<20}")
    for i in range(1, 11):

        execTimeR1 = measureExecutionTime(r1, i)
        execTimeR2 = measureExecutionTime(r2, i)
        execTimeR3 = measureExecutionTime(r3, i)
        execTimeR4 = measureExecutionTime(r4, i)
    
        print(f"{i:<5}{execTimeR1:<20}{execTimeR2:<20}{execTimeR3:<20}{execTimeR4:<20}")

main()