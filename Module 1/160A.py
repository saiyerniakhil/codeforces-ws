n = int(input())
n_coins = [int(i) for i in input().split(" ")]

"""
3 3 -> total sum = 6 -> target more than  6 / 2 = 3 -> 

"""
def getMinCoins(n, n_coins):
    n_coins = sorted(n_coins, reverse=True)
    sum_n = sum(n_coins)
    target_sum = sum_n // 2
    sums = 0
    for i in range(n):
        sums += n_coins[i]
        if(sums > target_sum):
            return i + 1

print(getMinCoins(n, n_coins))

# print(getMinCoins(3, [2, 1, 2]))
# print(getMinCoins(2, [3, 3]))
# print(getMinCoins(5, [5, 2, 1, 3, 4]))

"""
    5, 2, 1, 3, 4 --> 5, 4, 3, 2, 1 -> [15 // 2 = 7] -> 2 (Answer)
"""

