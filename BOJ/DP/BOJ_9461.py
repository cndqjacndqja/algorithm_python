t = int(input())


for j in range(t):
    n = int(input())
    dp = [0] * 101
    result = 1
    for i in range(n+1):
        if i < 4:
            dp[i] = 1
        elif 3 < i <6:
            dp[i] = 2
        else:
            dp[i] = dp[i-1] + dp[result]
            result+=1
    print(dp[n])