from functools import reduce 

n = int(input())
inputs = []

for i in range(n):
    x, y, z = input().split(" ")
    inputs.append((int(x), int(y), int(z)))

def sumVectors(v1, vsum):
    return (v1[0] + vsum[0], v1[1] + vsum[1], v1[2] + vsum[2])

def isVecorZeroSum(inputs):
    x1,y1,z1 = reduce(sumVectors, inputs)
    return "YES" if (x1 == 0 and y1 == 0 and z1 == 0) else "NO"

print(isVecorZeroSum(inputs))
