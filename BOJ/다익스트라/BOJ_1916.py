from heapq import heappush, heappop
import sys

n = int(input())
m = int(input())
data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    data[a].append((b, c))

start, end = map(int, input().split())
INF = int(1e9)
visited = [INF for _ in range(n + 1)]


def dijkstra():
    q = []
    q.append((0, start))
    visited[start] = 0

    while q:
        dis, node = heappop(q)

        if visited[node] < dis:
            continue
        for i in data[node]:
            cost = visited[node] + i[1]
            if cost < visited[i[0]]:
                visited[i[0]] = cost
                heappush(q, (cost, i[0]))

    print(visited[end])


dijkstra()
