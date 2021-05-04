from _collections import deque

n = int(input())
data = [[] for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]


for i in range(1, n + 1):
    value = list(map(int, input().split()))
    time[i] = value[0]
    indegree[i] += value[1]
    for j in value[2:]:
        data[j].append(i)

def topology_sort():
    q = deque()
    dp = [i for i in time]

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()

        for i in data[node]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[node] + time[i])

            if indegree[i] == 0:
                q.append(i)

    print(max(dp))

topology_sort()
