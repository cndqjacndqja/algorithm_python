for _ in range(int(input())):
    n = int(input())
    data = []
    for _ in range(2):
        data.append(list(map(int, input().split())))
    dp = [[0 for _ in range(n)] for _ in range(2)]

    dp[0][0] = data[0][0]
    dp[1][0] = data[1][0]

    for i in range(n):
        dp[0][i] = max(dp[1][i - 1] + data[0][i], dp[1][i - 2] + data[0][i])
        dp[1][i] = max(dp[0][i - 1] + data[1][i], dp[0][i - 2] + data[1][i])

    print(max(dp[0][n - 1], dp[1][n - 1]))
