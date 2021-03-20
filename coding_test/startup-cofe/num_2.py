import time
from _collections import deque

n = int(input())
data = list(map(int, input()))
start_time = time.time()


def bfs():
    dp = [0 for _ in range(n)]

    dp[0] = data[0]
    dp[1] = data[1]

    for i in range(2, n):
        if data[i] == 1:
            if data[i-1] == 1:
               dp[i] += dp[i-1]
            if data[i-2] == 1:
                dp[i] += dp[i-2]

    print(dp[n-1])
bfs()
