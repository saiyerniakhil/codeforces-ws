from collections import Counter

# def canConstruct( ransomNote: str, magazine: str) -> bool:
#         counter_rn = Counter(ransomNote)
#         counter_mg = Counter(magazine)

#         for (key, value) in counter_rn.items():
#             print(key, value)
#             if key in counter_mg.keys(): 
#                 if counter_mg[key] >= value:
#                     continue
#                 else:
#                     return False
#             else:
#                 return False

# print(canConstruct("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))

def wordPattern(pattern: str, s: str) -> bool:
        pattern_counter = Counter(list(pattern))
        s_counter = Counter(s.split(" "))

        if (len(pattern_counter.keys()) != len(s_counter.keys())):
            return False
        else:
            s_copy = s
            for i,j in zip(s_counter.keys(), pattern_counter.keys()):
                s_copy = s_copy.replace(i, j) 
            
            if(s_copy.replace(" ", "") != pattern):
                return False   
        return True

print(wordPattern("abc", "b c a"))
