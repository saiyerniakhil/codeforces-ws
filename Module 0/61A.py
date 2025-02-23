one = input()
two = input()

def findCorrespondingNumber(a, b):
    return format(int(a, 2) ^ int(b, 2), f"0{len(a)}b")

print(findCorrespondingNumber(one, two))