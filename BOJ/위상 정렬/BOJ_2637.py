from _collections import deque

n = int(input())
m = int(input())
distance = [0 for _ in range(n + 1)]
data = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
connecting = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    connecting[b].append((a, c))
    distance[a] += 1

q = deque()
for i in range(1, n + 1):
    if distance[i] == 0:
        q.append(i)

while q:
    pop_node = q.popleft()

    for i in connecting[pop_node]:
        node, count = i
        if data[pop_node].count(0) == n + 1:
            data[node][pop_node] += count
        else:
            for j in range(1, n+1):
                data[node][j] += data[pop_node][j] * count
        distance[node] -= 1
        if distance[node] == 0:
            q.append(node)

for i in range(1, n+1):
    if data[n][i] != 0:
        print(i, data[n][i])