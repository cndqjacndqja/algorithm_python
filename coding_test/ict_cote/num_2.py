from collections import Counter
from itertools import permutations

def getMinDelections(s):
    c = Counter(s)
    count = 0
    for i in c:
        if c[i] > 1:
            count += c[i] - 1
    return count

s = input()
print(getMinDelections(s))
