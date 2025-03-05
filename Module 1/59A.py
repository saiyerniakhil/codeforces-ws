from collections import Counter

text = input()

def convert(t):
    isUpperCase = lambda c: True if (65 <= ord(c) <=90) else False

    counts = {"uc": 0, "lc": 0}

    for i in list(t):
        if (isUpperCase(i)):
            counts['uc'] += 1
        else:
            counts['lc'] += 1

    return t.upper() if (counts['uc'] > counts['lc']) else t.lower()

print(convert(text))