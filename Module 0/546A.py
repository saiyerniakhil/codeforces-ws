k, n , w = [int(i) for i in input().split(" ")]

def howMuchToBorrow(k, n, w):
    costOfW = ((w * (w + 1)) / 2) * k
    remainingCost = n - costOfW
    if(remainingCost < 0):
        return int(-1 * remainingCost)
    else:
        return 0

print(howMuchToBorrow(k, n, w))