from collections import deque


def reachTheEnd(grid, maxTime):
    q = deque()
    row, low = len(grid), len(grid[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[0 for _ in range(low)] for _ in range(row)]
    visited[0][0] = 0
    q.append((0, 0))

    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < row and 0 <= ny < low and visited[nx][ny] == 0 and grid[nx][ny] == '.':
                visited[nx][ny] = visited[pop_x][pop_y] + 1
                q.append((nx, ny))

    if visited[row - 1][low - 1] != 0 and visited[row - 1][low - 1] <= maxTime or (row - 1 == 0 and low - 1 == 0):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    n = int(input())
    data = []
    for _ in range(n):
        data.append(input())
    time = int(input())
    reachTheEnd(data, time)
