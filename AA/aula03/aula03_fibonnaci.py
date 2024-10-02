def fibonnaciRec(n, count = 0):

    if n == 0 or n == 1:
        return n, count
    
    # if n == 2:
    #     return 1

    count += 1
    result1, count = fibonnaciRec(n-1, count)
    result2, count = fibonnaciRec(n-2, count)
    return result1 + result2 ,count

def fibonnaciDP1(n): # dynamic programming 1 with an array (version 2)
    
    fibonnaci = [0] * (n+1) # creates an array with size n+1
    count = 0
    
    if n >= 0:
        fibonnaci[0] = 0
    if n >= 1:
        fibonnaci[1] = 1

    for i in range(2, n+1):
        fibonnaci[i] = fibonnaci[i-1] + fibonnaci[i-2]
        count += 1 # add addition
    
    return fibonnaci[n], count # returns the sum of the nth fibonnaci

def fibonnaciDP2(n): # dynamic programming 2 with 3 variables (version 3)
    
    fibonnaci1, fibonnaci2 = 0, 1
    count = 0

    if n == 0:
        return 0, 0
    
    for i in range(2, n+1):
        fibonnaci = fibonnaci1 + fibonnaci2
        count += 1
        fibonnaci1 = fibonnaci2
        fibonnaci2 = fibonnaci

    return fibonnaci2, count # fibonnaci2 turns the value of the last sum, the result

def main():
    print("Fibonnaci with recursion")
    print(f"{'n':<5}{'r fibonnaci(n)':<20}{'additions':<20}")
    for i in range (11):
        r, count = fibonnaciRec(i)
        # print(r)
        print(f"{i:<5}{r:<20}{count:<20}") # exponencial growth

    print()
    print("Fibonnaci with dymanic programming - array")
    print(f"{'n':<5}{'r fibonnaci(n)':<20}{'additions':<20}")
    for i in range (11):
        r, count = fibonnaciDP1(i)
        print(f"{i:<5}{r:<20}{count:<20}")

    print()
    print("Fibonnaci with dymanic programming - variables")
    print(f"{'n':<5}{'r fibonnaci(n)':<20}{'additions':<20}")
    for i in range (11):
        r, count = fibonnaciDP2(i)
        print(f"{i:<5}{r:<20}{count:<20}")
    
main()