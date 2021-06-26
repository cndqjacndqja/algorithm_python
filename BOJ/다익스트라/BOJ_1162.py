from heapq import heappush, heappop

n, m, k = map(int, input().split())
INF = int(1e9)

visited = [[False for _ in range(k + 1)] for _ in range(n + 1)]
distance = [[INF for _ in range(k + 1)] for _ in range(n + 1)]
data = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

q = []
heappush(q, (0, 1, k))
for i in range(k + 1):
    distance[1][i] = 0

while q:
    dis, pop_node, k = heappop(q)

    if visited[pop_node][k]:
        continue
    visited[pop_node][k] = True

    for next_node, next_dis in data[pop_node]:
        if dis + next_dis < distance[next_node][k]:
            distance[next_node][k] = dis + next_dis
            heappush(q, (distance[next_node][k], next_node, k))
        if k > 0:
            if distance[next_node][k - 1] > distance[pop_node][k]:
                distance[next_node][k - 1] = distance[pop_node][k]
            heappush(q, (distance[next_node][k - 1], next_node, k - 1))
print(min(distance[-1]))

