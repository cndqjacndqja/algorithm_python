n, m = map(int, input().split())
data = list(map(int, input().split()))
visited = [False for _ in range(n)]
result = 0


def dfs(cnt, idx, param_data):
    global result
    if cnt == 3:
        if param_data <= m:
            result = max(result, param_data)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, i + 1, param_data + data[i])
            visited[i] = False


dfs(0, 0, 0)
print(result)
