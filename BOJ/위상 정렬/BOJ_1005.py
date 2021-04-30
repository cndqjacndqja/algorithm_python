from _collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    time = list(map(int, input().split()))
    data = [[] for _ in range(n+1)]
    indegree = [0 for _ in range(n+1)]
    for _ in range(k):
        a, b = map(int, input().split())
        data[a].append(b)
        indegree[b] += 1
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append((i, 0))

    result = [0 for _ in range(n+1)]
    goal = int(input())
    while q:
        node, level = q.popleft()

        result[level] = max(result[level], time[node-1])
        if goal == node:
            result[level] = time[node-1]
            break

        for i in data[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append((i, level+1))


    print(sum(result))





