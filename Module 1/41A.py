berlandish = input()
birlandish = input()

def isTranslatedCorrectly(ins, out):
    if ins == out[::-1]:
        return "YES"
    else:
        return "NO"
    
print(isTranslatedCorrectly(berlandish, birlandish))