import sys

sys.setrecursionlimit(100000)

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def search(h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] > h and visited[i][j] == False:
                visited[i][j] = True
                count += 1
                dfs2(i, j, visited, h)
    return count


def dfs2(x, y, visited, h):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and data[nx][ny] > h:
            visited[nx][ny] = True
            dfs2(nx, ny, visited, h)


def dfs(x, y, visited, h):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if visited[x][y] == False and data[x][y] > h:
        visited[x][y] = True
        dfs(x - 1, y, visited, h)
        dfs(x + 1, y, visited, h)
        dfs(x, y - 1, visited, h)
        dfs(x, y + 1, visited, h)
        return True
    return False


def solved():
    result = []
    for i in range(101):
        result.append(search(i))
    print(max(result))


solved()
