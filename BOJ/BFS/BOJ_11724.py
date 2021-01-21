from _collections import deque

n, m = map(int, input().split())

data = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

q = deque()
visited = [False for _ in range(n + 1)]

result = 0
for i in range(1, n + 1):
    if visited[i] == False:
        q.append(i)
        visited[i] = True
        result += 1
        while q:
            index = q.popleft()

            for node in data[index]:
                if visited[node] == False:
                    visited[node] = True
                    q.append(node)

print(result)
