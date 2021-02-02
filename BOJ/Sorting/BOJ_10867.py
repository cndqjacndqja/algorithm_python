n = int(input())

data = list(map(int, input().split()))
data.sort()
data = list(set(data))
for i in data:
    print(i, end=' ')
