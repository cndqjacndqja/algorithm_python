INF = int(1e9)
n, m = map(int, input().split())

data = [[INF for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    data[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            data[a][b] = min(data[a][b], data[a][k]+data[b][k])

for i in data:
    print(i)
