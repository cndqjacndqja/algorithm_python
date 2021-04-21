from _collections import deque
from heapq import heappush, heappop

n, m = map(int, input().split())
INF = int(1e9)
dp = [INF for _ in range(100001)]
max_size = 100001


def solved():
    dp[n] = 0
    q = deque()
    q.append(n)

    while q:
        pop_data = q.popleft()
        if pop_data == m:
            print(dp[pop_data])
            break
        if 0 <= pop_data - 1 < max_size and dp[pop_data - 1] > dp[pop_data] + 1:
            dp[pop_data - 1] = dp[pop_data] + 1
            q.append(pop_data - 1)

        if 0 <= pop_data + 1 < max_size and dp[pop_data + 1] > dp[pop_data] + 1:
            dp[pop_data + 1] = dp[pop_data] + 1
            q.append(pop_data + 1)

        if 0 <= pop_data * 2 < max_size and dp[pop_data * 2] > dp[pop_data]:
            dp[pop_data * 2] = dp[pop_data]
            q.append(pop_data * 2)



solved()
