from _collections import deque

n = int(input())
data = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 1. 처음부터 bfs를 돌고, result에 카운트 값을 넣는다.

def bfs(x, y, visited):
    q = deque()
    visited[x][y] = True
    q.append((x, y))
    count = 1
    while q:
        pop_x, pop_y = q.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1 and visited[nx][ny] == False:
                q.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count

def solved():
    result = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1 and visited[i][j] == False:
                count = bfs(i, j, visited)
                result.append(count)
    print(len(result))
    result.sort()
    for i in result:
        print(i)

solved()


