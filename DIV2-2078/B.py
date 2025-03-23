n_test = int(input())
res = []

def distanceSum(arr):
    l = len(arr)
    sums = 0
    for i in arr:
        sums += l - i
    
    return sums
        

def teleport(t):
    # teleport the element i, given n - len of the array
    i, n = t
    if i == n:
        print(">>", i, n - 1)
        return n - 1
    else:
        return n

def areAtSamePlace(arr):
    for i in range(0, len(arr)):
        if ((i + 1) == arr[0]):
            return True
    return False



def findMinPossibleSum(n, k):
    arr = list(range(1, n + 1))[:]
    min_sum, min_sum_arr = distanceSum(arr), arr
    for i in range(k):
        arr = list(map(teleport, list(zip(arr, [n]*n))))[:]
        temp = distanceSum(arr)
        if temp <= min_sum:
            if (not(arr.count(n) > 1)):
                min_sum_arr = arr
                min_sum = temp
    return map(lambda x: str(x), min_sum_arr)
        

results = []

for i in range(n_test):
    n, k = [int(i) for i in input().split(" ")]
    results.append(findMinPossibleSum(n, k))

for i in results:
    print(" ".join(i))

