import math
x = [int(i) for i in input().split(" ")]

def findYear(a, b):
    if (a == b):
        return 1
    else:
        res = math.ceil(math.log(b/a)/math.log(3/2))
        if a * math.pow(3, res) == b * math.pow(2, res):
            res = res + 1
        return res
a, b = x
print(findYear(a, b))