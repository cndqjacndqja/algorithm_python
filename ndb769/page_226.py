n, m = map(int, input().split())

price = [int(input()) for _ in range(n)]

data = [10001] * (m+1)
data[0] = 0

for i in range(n):
    for j in range(1, m+1):
        if data[j - price[i]] != 10001:
            data[j] = min(data[j], data[j-price[i]]+1)

print(data[m])