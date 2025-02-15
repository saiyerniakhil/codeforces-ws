# Tidy the input
"""
4 (t test cases)
4 (test case 1 starts, length of the input array)
11 13 11 11 (input 1)
5 (test case 2 starts)
1 4 4 4 4 (input 2)
10 (test case 3)
3 3 3 3 10 3 3 3 3 3 (input 3)
3 (test case 4)
20 20 10 (input 4)
"""

tests = int(input())
inputs = []

def findTheSpy(nums):
    counts = {}
    for i in nums:
        if i in counts.keys():
            counts[i] = counts[i] + 1
        else:
            counts[i] = 1
            
    one, two = counts.items()

    if (one[1] == 1):
        return nums.index(one[0]) + 1
    if (two[1] == 1):
        return nums.index(two[0]) + 1

for test in range(tests):
    n = int(input())
    arr = [int(i) for i in input().split(" ")]
    
    inputs.append(arr)


for inp in inputs:
    print(findTheSpy(inp))




