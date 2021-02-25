from itertools import permutations

data = input().split()
print(list(map(''.join, permutations(data))))


