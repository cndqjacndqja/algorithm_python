from _collections import deque

n, m = map(int, input().split())

dx, dy = [-2, -1, 1, 2], [1, 2, 2, 1]

visited = [[0 for _ in range(m)] for _ in range(n)]
x, y = n - 1, 0


def bfs(param_x, param_y):
    q = deque()
    q.append((param_x, param_y))
    result = 0
    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                visited[nx][ny] = visited[pop_x][pop_y] + 1
                q.append((nx, ny))
                result = max(result, visited[nx][ny])

    return result


print(bfs(x, y))