# calculate delannoy numbers in a geometrical representation
# can move in N, E and NE directions
import time

def delannoyNumbersRec(m, n, count=0):
    
    if m == 0 or n == 0:
        return 1, count
    
    count += 2 # two additions

    result1, count = delannoyNumbersRec(m-1, n, count)
    result2, count = delannoyNumbersRec(m-1, n-1, count)
    result3, count = delannoyNumbersRec(m, n-1, count)

    return result1 + result2 + result3, count # calculate delannoy numbers

def main():
    m = 5
    n = 5
    print("Delannnoy Numbers with recursion")
    print(f"{'m':<5}{'n':<5}{'r delannoyNumbers(n)':<30}{'additions':<20}{'time':<20}")
    seconds = time.time()
    r, count = delannoyNumbersRec(m, n)
    print(f"{m:<5}{n:<5}{r:<30}{count:<20}{seconds:<20}")

main()