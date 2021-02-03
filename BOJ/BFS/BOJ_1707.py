from _collections import deque

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    data = [[] for _ in range(v+1)]
    visited = [False for _ in range(v+1)]
    q = deque()

    for _ in range(e):
        x, y = map(int, input().split())
        data[x].append(y)
        data[y].append(x)

    for i in data[1]:
        q.append(i)
    visited[1] = True

    result = True

    while q:
        index = q.popleft()

        if visited[index] == True:
            result = False
        visited[index] = True

        for i in data[index]:
            if visited[i] == False:
                q.append(i)

    if result:
        print("YES")
    else:
        print("NO")