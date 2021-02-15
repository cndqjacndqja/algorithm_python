n = int(input())

data = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

visited = [False for _ in range(n + 1)]
check = [[] for _ in range(n + 1)]


def dfs(start):
    stack = [start]

    while stack:
        node = stack.pop()
        visited[node] = True

        for i in data[node]:
            if not visited[i]:
                stack.append(i)
                check[i] = node


dfs(1)
for i in range(2, n+1):
    print(check[i])


