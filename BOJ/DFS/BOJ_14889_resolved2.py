n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

check = [False for _ in range(n)]
result = []

def dfs(cnt, x):
    if cnt == n // 2:
        result.append(cal())
        return

    for i in range(x, n):
        if not check[i]:
            check[i] = True
            dfs(cnt+1, i)
            check[i] = False


def cal():
    team1 = []
    team2 = []

    for i in range(n):
        if not check[i]:
            team1.append(i)
        else:
            team2.append(i)

    sum1 = 0
    sum2 = 0
    for i in team1:
        for j in team1:
            sum1 += data[i][j]

    for i in team2:
        for j in team2:
            sum2 += data[i][j]

    return abs(sum1-sum2)

dfs(0, 0)
print(min(result))