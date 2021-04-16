if __name__ == "__main__":
    T = int(input())
    dp = [0 for i in range(0, 13)]

    def fibonacci(n):
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for i in range(4, n+1):
            if dp[i] is 0:
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]


    for i in range(0, T):
        n = int(input())
        print(fibonacci(n))