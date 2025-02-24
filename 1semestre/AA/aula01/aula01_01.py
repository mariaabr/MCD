# algoritmos interativos

def f1(n):
    r = 0
    for i in range(1, n+1):
        r += i
    return r

def f2(n):
    r = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            r += 1
    return r

def f3(n):
    r = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            r += 1
    return r

def f4(n):
    r = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            r += j
    return r
    
def main():
    print("function f1: ")
    # for i in range(1, 11):
    #     print("i ", i) + print(f1(i))
    
    print(f"{'n':<5}{'r f1(n)':<20}")
    for i in range(1, 11):
        print(f"{i:<5}{f1(i):<20}")

    print("function f2: ")
    # for i in range(1, 11):
    #     print("i", i) + print(f2(i))

    print(f"{'n':<5}{'r f2(n)':<20}")
    for i in range(1, 11):
        print(f"{i:<5}{f2(i):<20}")

    print("function f3: ")
    # for i in range(1, 11):
    #     print("i", i) + print(f3(i))

    print(f"{'n':<5}{'r f3(n)':<20}")
    for i in range(1, 11):
        print(f"{i:<5}{f3(i):<20}")
    
    print("function f4: ")
    # for i in range(1, 11):
    #     print("i", i) + print(f4(i))

    print(f"{'n':<5}{'r f4(n)':<20}")
    for i in range(1, 11):
        print(f"{i:<5}{f4(i):<20}")

    print("all results in one table:")
    print(f"{'n':<5}{'r f1(n)':<20}{'r f2(n)':<20}{'r f3(n)':<20}{'r f4(n)':<20}")
    for i in range(1, 11):
        print(f"{i:<5}{f1(i):<20}{f2(i):<20}{f3(i):<20}{f4(i):<20}")

main()