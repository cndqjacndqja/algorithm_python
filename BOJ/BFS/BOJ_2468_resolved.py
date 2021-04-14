from _collections import deque

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(h):
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == False and data[i][j] > h:
                spread(i, j, visited, h)
                count += 1
    return count


def spread(x, y, visited, h):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 0

    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False and data[nx][ny] > h:
                count += 1
                visited[nx][ny] = True
                q.append((nx, ny))

    return count


def solved():
    result = []
    for i in range(101):
        result.append(bfs(i))
    print(max(result))


solved()
