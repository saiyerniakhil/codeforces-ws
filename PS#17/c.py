"""


"""

ntests = int(input())
inputs = []

for test in range(ntests):
    n = int(input())
    arr = [int(i) for i in input().split(" ")]
    
    inputs.append(arr)

   
"""
upvote -> +1
downvote -> -1
"""
def reviewSite(reviewers):
    server_1 = 0
    server_2 = 0

    for r in reviewers:
        if r == 1:
            if server_1 > server_2 and server_1 > 0:
                # send to server_1
                server_1 += 1
            else:
                server_2 += 1
        elif r == 2:
            if server_1 > server_2 and server_1 > 0:
                # send to server_1
                server_2 -= 1
            else:
                server_1 -= 1
        elif r == 3:
            if server_1 > server_2:
                server_1 += 1
            else:
                server_2 += 1

    return server_1 if server_1 > server_2 else server_2

for inp in inputs:
   print(reviewSite(inp))
