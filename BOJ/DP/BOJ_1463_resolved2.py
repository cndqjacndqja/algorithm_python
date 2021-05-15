import sys
sys.setrecursionlimit(1000000)
INF = int(1e9)
n = int(input())
dp = [INF for _ in range(n + 1)]
dp[n] = 0


def recursive(num):
    if num <= 1:
        return

    if num % 3 == 0 and dp[num // 3] > dp[num] + 1:
        dp[num // 3] = dp[num] + 1
        recursive(num // 3)
    if num % 2 == 0 and dp[num // 2] > dp[num] + 1:
        dp[num // 2] = dp[num] + 1
        recursive(num // 2)
    if dp[num - 1] > dp[num] + 1:
        dp[num - 1] = dp[num] + 1
        recursive(num - 1)


recursive(n)
print(dp[1])
