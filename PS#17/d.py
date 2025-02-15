import math

f = open("input.txt")


ntests = int(f.readline().strip())
inputs = []

for test in range(ntests):
    nlines = int(f.readline().strip())
    arr = []
    for l in range(nlines):
        line = list(f.readline().strip())
        arr.append(line)
    inputs.append(arr)

def mapCoordinates(arr):
    coords = [] # (x1, y1), (x2, y2)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j] == "*"):
                coords.append((i, j))
    return coords 

def distance(point1, point2):
    x1,y1 = point1
    x2, y2 = point2
    d = int(round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)))
    return d

def findOtherCoordinates(coords):
    (x1, y1), (x2, y2) = coords
    # opposite
    if (x1 == y1 and x2 == y1):
        pass
    # on the same side
    elif (x2 == x1 or y1 == y2):
        pass
        


for inp in inputs:
    print(findOtherCoordinates(inp))
    