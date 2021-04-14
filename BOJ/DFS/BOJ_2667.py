n = int(input())
data = [list(map(int, input())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

result = []
count = 0


def dfs(x, y):
    global count
    if 0 > x or x >= n or 0 > y or y >= n:
        return
    if data[x][y] == 1:
        count += 1
        data[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j):
            result.append(count)
            count = 0

result.sort()
print(len(result))
for i in result:
    print(i)
