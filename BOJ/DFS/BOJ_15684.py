n, m, h = map(int, input().split())
data = [[0 for _ in range(h + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[b][a] = 1


def move():
    for i in range(1, n + 1):
        x = i
        for j in range(1, h + 1):
            if data[x][j] == 1:
                if x + 1 <= n:
                    x += 1
            elif 0 < x - 1 <= n and data[x - 1][j] == 1:
                x -= 1

        if x != i:
            return 0
    return 1

max_size = int(1e9)
result = max_size


def dfs(cnt, idx, r):
    global result
    if cnt == r:
        if move():
            result = min(cnt, result)
            return 1
        else:
            return 0

    for i in range(idx, n):
        for j in range(1, h + 1):
            if data[i][j] == 1:
                continue
            elif 0 < i - 1 <= n and data[i - 1][j] == 1:
                continue
            data[i][j] = 1
            dfs(cnt + 1, i, r)
            data[i][j] = 0


def solved():
    for i in range(4):
        dfs(0, 1, i)

    if result == max_size:
        print(-1)
    else:
        print(result)

solved()
