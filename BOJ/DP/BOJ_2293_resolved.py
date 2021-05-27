n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

counts = [0 for _ in range(k+1)]
counts[0] = 1

for coin in data:
    for price in range(k+1):
        if price >= coin:
            counts[price] += counts[price-coin]

print(counts[k])
