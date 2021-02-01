from _collections import deque

n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]
shark_size = 2
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0
size_count = 0


def search_fish():
    result = n ** 3
    nx, ny = 0, 0
    global cnt
    global shark_size
    global shark_point
    global size_count

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                if data[i][j] < shark_size:
                    move_size = bfs(i, j)

                    if result > move_size:
                        result = move_size
                        nx, ny = i, j

    if result == n ** 3:
        return False
    else:
        cnt += result
        size_count += 1
        if size_count == shark_size:
            size_count = 0
            shark_size += 1
        data[nx][ny] = 0
        shark_point = (nx, ny)
        return True


# 해당 지점까지 길이 구하기.
def bfs(point_x, point_y):
    shark_x, shark_y = shark_point
    visited = [[0 for _ in range(n)] for _ in range(n)]

    q = deque()
    q.append((shark_x, shark_y))
    while q:
        px, py = q.popleft()

        if px == point_x and py == point_y:
            data[shark_x][shark_y] = 0
            return visited[px][py]

        for i in range(4):
            nx, ny = px + dx[i], py + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and data[nx][ny] <= shark_size:
                visited[nx][ny] = visited[px][py] + 1
                q.append((nx, ny))

    return n ** 3


shark_point = (0, 0)

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark_point = (i, j)

while True:
    if search_fish() == False:
        print(cnt)
        break
