n = int(input())
m = int(input())
data = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False for _ in range(n + 1)]


def dfs(idx):
    for i in data[idx]:
        if not visited[i]:
            visited[i] = True # 이렇게 되면 어떤 의미이지?,
            # 뒤에 visited[i] = False는 방문하지 않고, 다음 것을 방문 헸을 때의 의미이다.

            dfs(i)


dfs(1)
result = 0
for i in range(2, n + 1):
    if visited[i]:
        result += 1
print(result)
