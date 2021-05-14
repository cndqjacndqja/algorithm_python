dp = [0 for _ in range(46)]
def recursive(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    if dp[num] != 0:
        return dp[num]
    dp[num] = recursive(num - 1) + recursive(num - 2)
    return dp[num]


n = int(input())
print(recursive(n))
