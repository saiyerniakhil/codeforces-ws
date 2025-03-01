from collections import Counter
x = input()
s = input()

def checkWinner(s):
    counts = Counter(list(s))
    if counts['A'] > counts['D']:
        return "Anton"
    elif counts['D'] > counts['A']:
        return "Danik"
    else:
        return "Friendship"

print(checkWinner(s))
