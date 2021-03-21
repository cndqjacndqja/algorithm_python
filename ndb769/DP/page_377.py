n = int(input())
data = []
dp = [0 for _ in range(n)]
for _ in range(n):
    data.append(list(map(int, input().split())))


def solve(i):
    if i > n - 1:
        return 0
    ret = 0
    if i + data[i][0] <= n:
        ret = solve(i + data[i][0]) + data[i][1]
    ret = max(ret, solve(i + 1))
    return ret


print(solve(0))
