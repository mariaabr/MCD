# how many ways can a robot move a distance of n meters?
# can move forward 1 meter, 2 meters or 3 meters

def linearRobotRec(n, count=0):
    
    if n == 0:
        return 0, count
    if n == 1:
        return 1, count
    if n == 2:
        return 2, count
    if n == 3:
        return 4, count # not 5 because order doesn't matter ?!
    
    count += 2 # two additions
    
    result1, count = linearRobotRec(n-1, count) # if it moves 1m, leave n-1 meters to still complete
    result2, count = linearRobotRec(n-2, count) # if it moves 2m, leave n-2 meters to still complete
    result3, count = linearRobotRec(n-3, count) # if it moves 3m, leave n-3 meters to still complete

    # any of the choices, to still complete can be by moving 1, 2 or 3 meters

    return result1 + result2 + result3, count # sum of the number of ways to move a distance of n

def linearRobotDP1(n):
    
    distance = [0] * (n+1)
    count = 0

    if n >= 0:
        distance[0] = 0
    if n >= 1:
        distance[1] = 1
    if n >= 2:
        distance[2] = 2
    if n >= 3:
        distance[3] = 4

    for i in range(4, n+1):
        distance[i] = distance[i-1] + distance[i-2] + distance[i-3]
        count += 2

    return distance[n], count

def linearRobotDP2(n):

    ways1, ways2, ways3 = 4, 2, 1 # ways1 = ways to reach 3 meters, ways2 = ways to reach 2 meter, ways3 = ways to reach 1 meters
    count = 0

    if n == 0:
        return 0, count
    if n == 1:
        return 1, count
    if n == 2:
        return 2, count
    if n == 3:
        return 4, count
    
    for i in range(4, n+1):
        linearRobot = ways1 + ways2 + ways3
        count += 2
        ways3 = ways2 # lower
        ways2 = ways1 # middle
        ways1 = linearRobot # higher

        # ways1 = ways2
        # ways2 = ways3
        # ways3 = linearRobot

    return ways1, count

def main():
    print("Linear Robot with recursion")
    print(f"{'n':<5}{'r linearRobot(n)':<20}{'additions':<20}")
    for i in range (11):
        r, count = linearRobotRec(i)
        # print(r)
        print(f"{i:<5}{r:<20}{count:<20}") # exponencial growth

    print()
    print("Linear Robot with dymanic programming - array")
    print(f"{'n':<5}{'r linearRobot(n)':<20}{'additions':<20}")
    for i in range (11):
        r, count = linearRobotDP1(i)
        print(f"{i:<5}{r:<20}{count:<20}")

    print()
    print("Linear Robot with dymanic programming - variables")
    print(f"{'n':<5}{'r linearRobot(n)':<20}{'additions':<20}")
    for i in range (11):
        r, count = linearRobotDP2(i)
        print(f"{i:<5}{r:<20}{count:<20}")
    
main()