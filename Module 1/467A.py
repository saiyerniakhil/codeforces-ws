n = int(input())
inputs = []

for i in range(n):
    x,y = input().split(" ")
    inputs.append((int(x),int(y)))


def canAccommodateAlexAndGeorge(inputs):
    res = filter(lambda p: True if p[0] + 2 <= p[1] else False, inputs)
    return len(list(res))

print(canAccommodateAlexAndGeorge(inputs))