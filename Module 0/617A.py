n = int(input())

def getMinSteps( x):
    numOfSteps = 0
    for i in range(5, 0, -1):
        if x == 0:
            break
        numOfSteps += x // i
        x = x % i
    return numOfSteps

print(getMinSteps(n))