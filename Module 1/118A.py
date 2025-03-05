text = input()


# t o u r -> t r -> .t .r
# akhil -> k h l -> .k .h .l 
def stringTask(t):
    t = t.lower()
    isNotVowel = lambda c: not (c.lower() in ['a', 'e', 'i', 'o', 'u', 'y'])

    return '.' + '.'.join(list(filter(isNotVowel, list(t))))

# print(stringTask('akhil'))
# print(stringTask('codeforces'))
# print(stringTask('tour'))
print(stringTask(text))
