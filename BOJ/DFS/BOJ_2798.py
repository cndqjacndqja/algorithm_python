n, m = map(int, input().split())
data = list(map(int, input().split()))


def solved():
    dfs(0)
    print(m - sum_result)


result = [0 for _ in range(n)]
sum_result = int(1e9)
visited = [0 for _ in range(n)]


def dfs(cnt):
    global sum_result
    if cnt == 3:
        if sum(result) <= m:
            sum_result = min(sum_result, abs(sum(result) - m))
    else:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                result[i] = data[i]
                dfs(cnt + 1)
                visited[i] = 0
                result[i] = 0

solved()