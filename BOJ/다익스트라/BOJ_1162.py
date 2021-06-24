from heapq import heappush, heappop

n, m, k = map(int, input().split())
INF = int(1e9)
k += 1

visited = [[False for _ in range(k)] for _ in range(n)]
distance = [[INF for _ in range(k)] for _ in range(n)]
data = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    data[a-1].append((b-1, c))
    data[b-1].append((a-1, c))

q = []
heappush(q, (0, 0, k-1))
for i in range(k):
    distance[0][i] = 0

while q:
    _ , pop_node, k = heappop(q)
    if visited[pop_node][k]:
        continue
    visited[pop_node][k] = True

    for next_node, next_dis in data[pop_node]:
        if distance[pop_node][k] + next_dis < distance[next_node][k]:
            distance[next_node][k] = distance[pop_node][k] + next_dis
            heappush(q, (distance[next_node][k], next_node, k))
        if k > 0:
            if distance[next_node][k-1] > distance[pop_node][k]:
                distance[next_node][k-1] = distance[pop_node][k]
            heappush(q, (distance[next_node][k-1], next_node, k-1))
print(min(distance[-1]))


