from _collections import deque

INF = 1e9
n, m = map(int, input().split())

data = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a][b] = 1
    data[b][a] = 1

X, K = map(int, input().split())

for i in range(1, n + 1):
    data[i][i] = 0


def floyd_warshall():
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                data[a][b] = min(data[a][b], data[a][k] + data[k][b])
    print(data[1][K] + data[K][X])


floyd_warshall()
