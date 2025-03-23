tests_n = int(input())
outputs = []


def finalVerdict(n, x, arr):
    
    k = 1
    if x == sum(arr) / len(arr):
        return "YES"
    else:
        return "NO"


for i in range(tests_n):
    # read each and every test case 
    n, x = [int(x) for x in input().split(" ")]
    arr = [int(x) for x in input().split(" ")]
    outputs.append(finalVerdict(n, x, arr))

for i in outputs:
    print(i)