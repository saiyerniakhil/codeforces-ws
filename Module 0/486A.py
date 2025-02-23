import math
n = int(input())

def calFun(n):
    flag = 1 if n % 2 == 0 else -1
    return (flag ** n) * math.ceil(n / 2)
    

print(calFun(n))