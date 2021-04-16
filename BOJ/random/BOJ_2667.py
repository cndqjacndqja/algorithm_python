n = int(input())

graph = []
data = []


for _ in range(n):
    graph.append(list(map(int, input())))

count = 0


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        global count
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        count += 1
        return True
    return False


for i in range(n):
    for j in range(n):
        if dfs(i, j):
            data.append(count)
            count = 0

data.sort()
print(len(data))
for i in data:
    print(i)


