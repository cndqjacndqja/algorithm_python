from _collections import deque

n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

data = [list(map(int, input())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
item = [[1 for _ in range(m)] for _ in range(n)]


def print_data(name,data):
    print(name)
    for i in data:
        print(i)

    print("-----")


def bfs():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    while q:
        x, y = q.popleft()
        print_data("item", item)
        print(x, y)
        print_data("visited", visited)
        if x == n - 1 and y == m - 1:
            return visited[x][y]

        for i in range(4):
            move_x, move_y = x + dx[i], y + dy[i]
            if 0 <= move_x < n and 0 <= move_y < m and visited[move_x][move_y] == 0:
                if data[move_x][move_y] == 0:
                    q.append((move_x, move_y))
                    item[move_x][move_y] = item[x][y]
                    visited[move_x][move_y] = visited[x][y] + 1
                else:
                    if item[x][y] == 1:
                        item[move_x][move_y] = 0
                        q.append((move_x, move_y))
                        item[x][y] = 1
                        visited[move_x][move_y] = visited[x][y] + 1
    return -1


print(bfs())
