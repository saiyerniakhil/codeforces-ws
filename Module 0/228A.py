from collections import Counter
x = [int(i) for i in input().split(" ")]

def getDistinctHorseShoes(shoes):
    return 4 - len(Counter(shoes).keys())

print(getDistinctHorseShoes(x))