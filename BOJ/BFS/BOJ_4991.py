from _collections import deque

# 가장 적은 이동 횟수로 더러운 칸을 모두 깨끗히 치우는 법
# 더러우 ㄴ좌표를 본 후, 가장 가까운 곳 부터 간다?
# 왔던길을 다시 돌아가면 손해니까,,, 오른쪽에 있는 거나, 가장 왼쪽에 있는 것을 먼저??
# 거리가 가장 짧은 것을 우선 순위로 둘까?
# 근데 만약 거리가 같다면,,,? 그럼 어떻게 하지? 청소기 현재 자표가
# 아니면 모든 좌표를 전부 다 가볼까,,?

cleaner_x, cleaner_y = 0, 0
result_clear_x, result_clear_y = 9, 0
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]





# 쓰레기까지 이동
def move_to_trash(trash_x, trash_y):
    global cleaner_x, cleaner_y

    visited = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((cleaner_x, cleaner_y))
    visited[cleaner_x][cleaner_y] = 0

    while q:
        pop_x, pop_y = q.popleft()
        if pop_x == trash_x and pop_y == trash_y:
            cleaner_x, cleaner_y = pop_x, pop_y
            return visited[pop_x][pop_y]
        if visited[pop_x][pop_y] > min_result:
            return visited[pop_x][pop_y]

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and data[nx][ny] != 'x':
                visited[nx][ny] = visited[pop_x][pop_y] + 1
                q.append((nx, ny))

    return -1





# 넘어온 좌표로 계산하기
def count_clear(check):
    global trash_direction, cleaner_x, cleaner_y, min_result

    result_count = 0
    for i in check:
        x, y = trash_direction[i]
        result_count += move_to_trash(x, y)
    cleaner_x, cleaner_y = result_clear_x, result_clear_y
    min_result = min(min_result, result_count)



def dfs(idx, num):
    if idx == num:
        count_clear(orders)
        return

    for i in range(num):
        if not check[i]:
            orders[idx] = i
            check[i] = True
            dfs(idx + 1, num)
            check[i] = False


while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        exit()
    data = [list(input()) for _ in range(n)]
    result = []
    trash_direction = []
    for i in range(n):
        for j in range(m):
            if data[i][j] == "o":
                cleaner_x, cleaner_y = i, j
                result_clear_x, result_clear_y = i, j
            if data[i][j] == '*':
                trash_direction.append((i, j))
    min_result = int(1e9)
    orders = [0 for _ in range(len(trash_direction))]
    check = [False for _ in range(len(trash_direction))]
    dfs(0, len(trash_direction))
    print(min_result)
