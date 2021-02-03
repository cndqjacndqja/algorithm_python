t = int(input())

for _ in range(t):
    n = int(input())
    dp =[(0, 0) for _ in range(n+1)]
    if n >= 0:
        dp[0] =(1, 0)
    if n >= 1:
        dp[1] = (0, 1)
    if n >= 2:
        for i in range(2, n+1):
            x1, y1 = dp[i-1]
            x2, y2 = dp[i-2]
            dp[i] = (x1+x2, y1+y2)
    x, y = dp[n]
    print(x, y)