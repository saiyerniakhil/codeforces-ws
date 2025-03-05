n, k = [int(i) for i in input().split(" ")]
nums = [int(i) for i in input().split(" ")]

def nextRound(k, nums):
    return len(list(filter(lambda x: 0 < x and x >= nums[k - 1] , nums)))

print(nextRound(k, nums))