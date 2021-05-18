n, m = map(int, input().split())
data = list(map(int, input().split()))
result = 0


def dfs(visited, cnt, x, param_data):
    global result
    if cnt == 3:
        if param_data <= m:
            result = max(result, param_data)
        return
    for i in range(x, n):
        if not visited[i]:
            visited[i] = True
            dfs(visited, cnt + 1, i, param_data + data[i])
            visited[i] = False


def solved():
    visited = [False for _ in range(n)]
    dfs(visited, 0, 0, 0)
    print(result)


solved()
