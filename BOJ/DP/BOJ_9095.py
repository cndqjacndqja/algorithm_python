def solved(num):
    dp = [0 for _ in range(12)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[num]


for _ in range(int(input())):
    n = int(input())
    print(solved(n))
