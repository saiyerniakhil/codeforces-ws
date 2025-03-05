num, k = input().split(" ")

def wrongSub(n, k):
    for i in range(int(k)):
        if(n[-1] == "0"):
            n = n[:-1]
        else:
            n = str(int(n) - 1)
    return n

print(wrongSub(num, k))
