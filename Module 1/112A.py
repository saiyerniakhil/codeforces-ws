a = input()
b = input()

def areEqual(x, y):
    if x.lower() == y.lower():
        return 0
    elif y.lower() < x.lower():
        return 1
    else:
        return -1

print(areEqual(a, b))