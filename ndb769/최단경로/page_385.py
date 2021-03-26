n = int(input())
m = int(input())
INF = int(1e9)
data = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    data[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a][b] = min(c, data[a][b])


def floyd():
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                data[a][b] = min(data[a][b], data[a][k] + data[k][b])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if data[i][j] == INF:
                print(0, end=' ')
            else:
                print(data[i][j], end=' ')
        print()


floyd()
