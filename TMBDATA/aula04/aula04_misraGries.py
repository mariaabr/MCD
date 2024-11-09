# implementation of misra gries algorithm
import random

# N = 100
# M = 3
# stream = [random.randint(0,N) for _ in range(M)] + [2*N] + [random.randint(0,N) for _ in range(M)]
stream = [1, 1, 2, 3, 4, 5, 1, 1, 1, 5, 3, 3, 1, 1, 2] # order is important for the final aproximation result
m = len(stream)
k = 6 # if k = 6 we know and have an algorithm to know the top 5

aproxF = {} # aproxFionary to store aproximated frequency of variables
frequencyD = {} # aproxFionary to store actual frequency of variables

for a in stream:
    if a in aproxF:
        aproxF[a] += 1
    elif len(aproxF) < k-1:
        aproxF[a] = 1
    else:
        for key in list(aproxF.keys()):
            aproxF[key] -= 1
            
        if aproxF[key] == 0:
                aproxF.pop(key)

print(f'dictionary aproximation of frequency of variables: {aproxF}')

for b in stream:
    if b in frequencyD:
        frequencyD[b] += 1
    else:
        frequencyD[b] = 1

print(f'dictionary actual of frequency of variables: {frequencyD}')

for element in aproxF:
    error = abs(aproxF[element] - frequencyD[element])/frequencyD[element] # should be divided by m to kinda normalize the value to compare with the other errors
    print(f'error of aproximated to actual frequency of {element}: {round(error, 2)}')

    minValue = frequencyD[element] - (m/k)
    
    print(f'{minValue} <= {aproxF[element]} <= {frequencyD[element]}')