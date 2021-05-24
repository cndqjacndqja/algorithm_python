from _collections import deque

m, n = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
binary_data = [[[0, 0, 0, 0] for _ in range(m)] for _ in range(n)]


# 방의 갯수
def count_room():
    visited = [[False for _ in range(m)] for _ in range(n)]
    room_count = 0
    room_size = []

    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                room_size.append(bfs_visited(i, j, visited))
                room_count += 1

    return room_count, max(room_size), 0


# 방문처리
def bfs_visited(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1

    while q:
        pop_x, pop_y = q.popleft()
        direction = binary_data[pop_x][pop_y]
        for i in range(4):
            if direction[3 - i] == 0:
                nx, ny = pop_x+dx[3-i], pop_y +dy[3-i]
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1

    return count


# 이진수 변환 이거 포스팅하기
def change_binary(x):
    y = ""
    while x > 0:
        y = str(x % 2) + y
        x //= 2

    direction = [0, 0, 0, 0]
    count = 3
    for i in range(len(y) - 1, -1, -1):
        direction[count] = int(y[i])
        count -= 1
    return direction


for i in range(n):
    for j in range(m):
        d = change_binary(data[i][j])
        binary_data[i][j] = d

def solved():
    result1, result2, result3 = count_room()
    print(result1)
    print(result2)
    result = []

    for i in range(n):
        for j in range(m):
            for z in range(4):
                if binary_data[i][j][z] == 1:
                    binary_data[i][j][z] = 0
                    result1, result2, result3 = count_room()
                    binary_data[i][j][z] = 1
                    result.append(result2)

    print(max(result))
solved()



