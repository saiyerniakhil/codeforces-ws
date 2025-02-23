from collections import Counter
n = int(input())

def getNextBeautifulYear(x):
    for i in range(x + 1, x + 9001):
        if (len(Counter(list(str(i))).keys()) == 4):
            return i

print(getNextBeautifulYear(n))