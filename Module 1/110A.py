from collections import Counter
num = input()

def isNearlyLucky(num):
    counts = Counter(num)
    
    def isLucky(n): 
        sub_counter = Counter(str(n))
        s_keys = sorted(list(sub_counter.keys()))
        return s_keys == ['4','7'] or s_keys == ['4'] or s_keys == ['7']

    totalLuckyDigits = counts['4'] + counts['7']
    return "YES" if isLucky(totalLuckyDigits) else "NO"

print(isNearlyLucky(num))
    