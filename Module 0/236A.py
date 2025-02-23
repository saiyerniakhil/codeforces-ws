from collections import Counter

x = input()

def chatOrNoChat(x):
   return "CHAT WITH HER!" if len(Counter(list(x)).keys()) % 2 == 0 else "IGNORE HIM!"

print(chatOrNoChat(x))