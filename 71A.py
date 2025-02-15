import sys
MAX_LENGTH = 10


def shorten(word):
    # TODO:
    wlen = len(word)
    if(wlen > MAX_LENGTH):
        return word[0] + str(wlen - 2) + word[wlen-1]
    else:
        return word

n = int(input().strip())
inputs = []
for i in range(n):
    inputs.append(input().strip())


for word in inputs:
    print(shorten(word))