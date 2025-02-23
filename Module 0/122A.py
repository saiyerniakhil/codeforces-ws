from collections import Counter
n = int(input())

def isAlmostLucky(n):
   luckyNumbers = [4, 7, 47, 74, 444, 777, 447, 477, 744, 774]
   isDivisibleByLuckyNum = 0 in list(map(lambda x: n % x, luckyNumbers))
   counts = Counter(list(str(n))).keys()
   onlyHas4and7 = len(counts) and (4 in counts or 7 in counts)

   return "YES" if isDivisibleByLuckyNum or onlyHas4and7 else "NO"

print(isAlmostLucky(n))