n, m = map(int, input().split())
data = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)
visited = [False for _ in range(n + 1)]


def dfs(idx):
    for i in data[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i)


result = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        result += 1
print(result)
