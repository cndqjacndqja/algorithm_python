from _collections import deque

c, r = map(int, input().split())

data = [list(input()) for _ in range(c)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
water_queue = deque()
beaver_queue = deque()
beaver_visited = [[0 for _ in range(r)] for _ in range(c)]
water_visited = [[0 for _ in range(r)] for _ in range(c)]
glo_result = True


# 물을 한번만 퍼뜨려야 한다.
def water():
    water_cnt = len(water_queue)
    for _ in range(water_cnt):
        pop_x, pop_y = water_queue.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and data[nx][ny] == '.' and water_visited[nx][ny] == 0:
                water_queue.append((nx, ny))
                water_visited[nx][ny] = water_visited[pop_x][pop_y] + 1


def beaver_move():
    global glo_result

    beaver_cnt = len(beaver_queue)
    if beaver_cnt == 0:
        glo_result = False
        return True

    for _ in range(beaver_cnt):
        pop_x, pop_y = beaver_queue.popleft()
        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < c and 0 <= ny < r and water_visited[nx][ny] == 0 and data[nx][ny] != 'X' and beaver_visited[nx][ny] == 0:
                if data[nx][ny] == 'D':
                    beaver_visited[nx][ny] = beaver_visited[pop_x][pop_y] + 1
                    print(beaver_visited[nx][ny])
                    return True
                else:
                    beaver_visited[nx][ny] = beaver_visited[pop_x][pop_y] + 1
                    beaver_queue.append((nx, ny))
    return False


def solve():
    for i in range(c):
        for j in range(r):
            if data[i][j] == '*':
                water_queue.append((i, j))
            if data[i][j] == 'S':
                beaver_queue.append((i, j))
    result = False

    while not result:
        water()

        result = beaver_move()

    if not glo_result:
        print("KAKTUS")


solve()
