import copy
from heapq import heappush, heappop

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
round = 0
while True:
    n = int(input())
    round += 1
    if n == 0:
        break
    data = []
    for _ in range(n):
        data.append(list(map(int, input().split())))

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True

    q = []
    heappush(q, (data[0][0], 0, 0))
    while q:
        dis, x, y = heappop(q)
        if x == n - 1 and y == n - 1:
            print("Problem {0}: {1}".format(round, dis))
            break
        if data[x][y] < dis:
            continue
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                data[nx][ny] += dis
                visited[nx][ny] = True
                heappush(q, (data[nx][ny], nx, ny))
