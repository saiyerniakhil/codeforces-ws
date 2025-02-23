import math
n, k =  [int(i) for i in input().split(" ")]

def kThElementInTheSeries(n, k):
    # we'll only deal in indexes
    k = k - 1
    half = math.ceil(n / 2) - 1
    if k <= half:
        # odd
        pos = k
        res = ((2 * pos)) + 1
        return res
    elif k >= half:
        # even
        pos = (k) - half - 1
        res = ((2 * pos)) + 2
        return res

print(kThElementInTheSeries(n, k))
