from _collections import deque

INF = int(1e9)
for _ in range(int(input())):
    n, m = map(int, input().split())

    data = [[] for _ in range(n + 1)]
    dp = [INF for _ in range(n + 1)]
    weight = [0 for _ in range(n + 1)]
    distance = [0 for _ in range(n+1)]

    visited = [False for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        weight[a] += 1
        weight[b] += 1
        data[a].append((b, c))
        data[b].append((a, c))
    q = deque()

    for i in range(1, n + 1):
        if weight[i] == 1:
            q.append(i)
            node, dis = data[i][0]
            dp[i] = dis
            distance[i] = dis

    while q:
        pop_idx = q.popleft()

        for i in data[pop_idx]:
            node, dis = i
            if not visited[node]:
                visited[pop_idx] = True
                dp[pop_idx] = min(distance[pop_idx], dis)
                distance[node] += dp[pop_idx]
                weight[node] -= 1
                if weight[node] == 1:
                    q.append(node)
    sum = 0
    for i in data[1]:
        node, dis = i
        sum += dp[node]
    print(dp)
    print(sum)






