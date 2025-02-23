n = int(input())

inputs = []
for i in range(0,n):
    inp = [int(j) for j in input().split(" ")]
    inputs.append(inp)

# print(inputs)

def countSolvable(arr):
    count = 0
    for i in arr:
        if sum(i) >= 2:
            count += 1
    return count

print(countSolvable(inputs))