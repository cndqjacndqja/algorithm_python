import copy
from _collections import deque

dx, dy = [0, -1, 1], [1, 1, 1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    insert_data = list(map(int, input().split()))

    data = []
    for i in range(0, len(insert_data), m):
        data.append(insert_data[i:i + m])

    dp_data = copy.deepcopy(data)
    for i in range(n):
        q = deque()
        q.append((i, 0))
        while q:
            pop_x, pop_y = q.popleft()

            for i in range(3):
                nx, ny = pop_x + dx[i], pop_y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    dp_data[nx][ny] = max(dp_data[nx][ny], dp_data[pop_x][pop_y] + data[nx][ny])
                    q.append((nx, ny))

    result = 0
    for i in range(n):
        result = max(result, max(dp_data[i]))
    print(result)
