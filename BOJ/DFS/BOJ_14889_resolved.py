n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
check = [False for _ in range(n + 1)]
result = []


def dfs(check_data, cnt, x):
    if cnt == (n // 2):
        solution(check_data)
        return

    # 만약 x여도 되나? 꼭 1이아니여도 되지? 이거 블로깅
    for i in range(x, n):
        if not check_data[i]:
            check_data[i] = True
            dfs(check_data, cnt + 1, i)
            check_data[i] = False


def solution(check_data):
    team1 = []
    team2 = []
    for i in range(1, n + 1):
        if check_data[i]:
            team1.append(i)
        else:
            team2.append(i)

    # 왜 팀 전체를 더하는지 모르겠음.. 그냥 같은 원리라서 그런가?
    sum1 = 0
    sum2 = 0
    for i in team1:
        for j in team1:
            sum1 += data[i - 1][j - 1]

    for i in team2:
        for j in team2:
            sum2 += data[i - 1][j - 1]

    result.append(abs(sum2 - sum1))


def solved():
    dfs(check, 0, 1)
    print(min(result))


solved()
