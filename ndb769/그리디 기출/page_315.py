from itertools import combinations

n, m = map(int, input().split())

data = list(map(int, input().split()))

result = list(combinations(data, 2))

sum = 0
for i in result:
    x, y = i
    if x != y:
        sum += 1

print(sum)