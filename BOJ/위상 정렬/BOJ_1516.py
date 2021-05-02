from _collections import deque

n = int(input())
data = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    detail_data = list(map(int, input().split()))
    detail_data = detail_data[:len(detail_data) - 1]
    time[i] = detail_data[0]
    for j in range(1, len(detail_data)):
        data[detail_data[j]].append(i)
        indegree[i] += 1


def topology_sort():
    q = deque()
    dp = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        dp[i] = time[i]
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append((i, 0))

    while q:
        node = q.popleft()

        for i in data[node]:
            indegree[i] -= 1
            dp[i] = max(dp[node] + time[i], dp[i])

            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(dp[i])


topology_sort()
