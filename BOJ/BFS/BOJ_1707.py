from _collections import deque


def bfs(param_x):
    global visited
    q = deque()
    q.append(param_x)
    visited[param_x] = 1

    while q:
        pop_x = q.popleft()

        for z in data[pop_x]:
            if visited[z] == 0:
                visited[z] = visited[pop_x] * -1
                q.append(z)
            elif visited[z] == visited[pop_x]:
                return 1
    return 0


for _ in range(int(input())):
    v, e = map(int, input().split())
    data = [[] for _ in range(v + 1)]
    visited = [0 for _ in range(v + 1)]

    for _ in range(e):
        x, y = map(int, input().split())
        data[x].append(y)
        data[y].append(x)

    ans = 0
    for i in range(1, v + 1):
        if visited[i] == 0:
            ans = bfs(i)
            if ans == 1:
                break
    if ans == 0:
        print("YES")
    else:
        print("NO")
