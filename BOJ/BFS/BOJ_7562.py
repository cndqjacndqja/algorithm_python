from _collections import deque

t = int(input())

dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, -2, -1, 1, 2]



# dfs는 왜 안되지..? 일단 작성한 코드에는 문제가 있어서 무한루프를 돈다.
# 코드가 멀쩡해도 dfs안된다고 하는데 그 이유가 뭘까,,?포스팅하자.
def dfs(start_idx, target_idx, count, visited):
    global arr_count
    length = len(visited[0])
    start_x, start_y = start_idx
    target_x, target_y = target_idx
    visited[start_x][start_y] = True
    if start_x == target_x and start_y == target_y:
        arr_count.append(count)
        print(start_x, start_y)
        return

    for i in range(8):
        x_move, y_move = start_x + dx[i], start_y + dy[i]
        if 0 <= x_move < length and 0 <= y_move < length and visited[x_move][y_move] == False:
            visited[x_move][y_move] = True
            dfs((x_move, y_move), (target_x, target_y), count + 1, visited)
            visited[x_move][y_move] = False


def bfs(start_x, start_y, target_x, target_y):
    q = deque()
    q.append((start_x, start_y))
    visited = [[0 for _ in range(l)] for _ in range(l)]

    while q:
        start_x, start_y = q.popleft()

        if start_x == target_x and start_y == target_y:
            return visited[target_x][target_y]

        for i in range(8):
            x_idx, y_idx = start_x + dx[i], start_y + dy[i]
            if 0 <= x_idx < l and 0 <= y_idx < l and visited[x_idx][y_idx] == 0:
                q.append((x_idx, y_idx))
                visited[x_idx][y_idx] = visited[start_x][start_y] + 1


for _ in range(t):
    l = int(input())
    start = (map(int, input().split()))
    target = (map(int, input().split()))

    start_x, start_y = start
    target_x, target_y = target
    count = bfs(start_x, start_y, target_x, target_y)
    print(count)
