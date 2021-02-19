from _collections import deque


def bfs(param_x):
    q = deque()
    global visited
    q.append((param_x, 0))
    while q:
        pop_node, pop_parent = q.popleft()
        visited[pop_node] = True

        if check[pop_node] == check[pop_parent]:
            return False

        for i in data[pop_node]:
            if not visited[i]:
                q.append((i, pop_node))
                check[i] = check[pop_node] * -1

    return True


for _ in range(int(input())):
    v, e = map(int, input().split())
    data = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    check = [-1 for _ in range(v + 1)]
    check[0] = 0

    result = True

    for _ in range(e):
        x, y = map(int, input().split())
        data[x].append(y)
        data[y].append(x)

    for i in range(1, v + 1):
        if not visited[i]:
            check[i] = 1
            result = bfs(i)
    if result:
        print("YES")
    else:
        print("NO")