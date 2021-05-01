from _collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    data = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    dp = [0 for _ in range(n + 1)]

    for _ in range(k):
        a, b = map(int, input().split())
        data[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        node = q.popleft()

        for i in data[node]:
            indegree[i] -= 1
            dp[i] = max(dp[node] + time[i], dp[i])
            if indegree[i] == 0:
                q.append(i)
    goal = int(input())
    print(dp[goal])
