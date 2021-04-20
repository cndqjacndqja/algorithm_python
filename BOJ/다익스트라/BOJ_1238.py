import sys
from heapq import heappush, heappop

n, m, x = map(int, input().split())
data = [[] for _ in range(n + 1)]
INF = int(1e9)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    data[a].append((b, c))


def dijkstra(start, end):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    q = []
    heappush(q, (0, start))

    while q:
        dis, node = heappop(q)
        if distance[node] < dis:
            continue
        for i in data[node]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                heappush(q, (cost, i[0]))
                distance[i[0]] = cost

    return distance[end]

def solved():
    result = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        start = dijkstra(i, x)
        end = dijkstra(x, i)
        result[i] = start+end

    print(max(result))
solved()

