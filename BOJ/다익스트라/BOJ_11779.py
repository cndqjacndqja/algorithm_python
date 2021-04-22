from heapq import heappush, heappop

n = int(input())
m = int(input())
data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))

start, end = map(int, input().split())
INF = int(1e9)


def dijkstra():
    q = []
    heappush(q, (0, start))
    visited = [[] for _ in range(n + 1)]
    visited[start].append(start)
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0

    while q:
        dis, node = heappop(q)
        if distance[node] < dis:
            continue
        for i in data[node]:
            cost = dis + i[1]
            if distance[i[0]] > cost:
                heappush(q, (cost, i[0]))
                distance[i[0]] = cost

                visited[i[0]] = []
                for j in visited[node]:
                    visited[i[0]].append(j)
                visited[i[0]].append(i[0])
    print(distance[end])
    print(len(visited[end]))
    for i in visited[end]:
        print(i, end=' ')


dijkstra()
