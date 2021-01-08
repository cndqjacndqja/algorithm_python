n = int(input())
data = list(map(int, input().split()))

for i in range(3, n):
    if data[i] + data[i - 2] < data[i - 1]:
        data[i] = data[i - 1]
    else:
        data[i] = data[i] + data[i - 2]

print(data[n-1])
