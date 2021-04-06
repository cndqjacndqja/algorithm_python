from _collections import deque

for _ in range(int(input())):
    n = int(input())
    data_m = list(map(int, input().split()))
    data = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            data[data_m[i]][data_m[j]] = True
            indegree[data_m[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if data[a][b]:
            data[a][b] = False
            data[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            data[a][b] = True
            data[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break

    if len(q) >= 2:
        certain = False
        break
    now = q.popleft()
    result.append(now)
    for j in range(1, n + 1):
        if data[now][j]:
            indegree[j] -= 1
            if indegree[j] == 0:
                result.append(j)
    
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()
