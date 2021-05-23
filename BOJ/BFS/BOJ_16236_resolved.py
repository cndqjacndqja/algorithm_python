from _collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# count를 셀꺼고,
# 조건에 따라서 물고기를 잡아 먹어야 한다.
# 먹는 우선순위를 어떻게 정하지? 이게 포인트인 것 같다.
shark_size = 2
shark_x, shark_y = 0, 0
INF = int(1e9)
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark_x, shark_y = i, j
            data[i][j] = INF


# 먹을 수 있는 물고기 찾기
def find_fish():
    # 거리까지 고려해주기.
    length = INF
    point_x, point_y = -1, -1

    for i in range(n):
        for j in range(n):
            if data[i][j] < shark_size and data[i][j] != 0:
                if length > bfs_length(i, j):
                    length = bfs_length(i, j)
                    point_x, point_y = i, j

    return point_x, point_y, length


def bfs_length(x, y):
    q = deque()
    visited = [[-1 for _ in range(n)] for _ in range(n)]

    q.append((shark_x, shark_y))
    visited[shark_x][shark_y] = 0

    while q:
        pop_x, pop_y = q.popleft()
        if pop_x == x and pop_y == y:
            return visited[pop_x][pop_y]

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and (data[nx][ny] <= shark_size or data[nx][ny] == INF):
                q.append((nx, ny))
                visited[nx][ny] = visited[pop_x][pop_y] + 1
    return INF

def solved():
    global shark_x, shark_y, shark_size
    result = 0
    flag = True
    count = 0

    while flag:
        point_x, point_y, length = find_fish()

        if point_x == -1 and point_y == -1:
            flag = False
        else:
            data[shark_x][shark_y] = INF
            data[point_x][point_y] = INF
            shark_x, shark_y = point_x, point_y
            result += length
            count += 1
            if count == shark_size:
                shark_size+=1
                count = 0

    print(result)

solved()


# 먹고 커지기
#
