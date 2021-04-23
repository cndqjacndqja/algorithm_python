from heapq import heappush, heappop

INF = int(1e9)


def dijkstra(start):
    q = []
    heappush(q, (0, start))
    visited = [1 for _ in range(n + 1)]
    distance = [INF for _ in range(n + 1)]
    distance[start] = 0

    while q:
        dis, node = heappop(q)
        for i in data[node]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
                visited[i[0]] = visited[node] + 1

    max_dis = 0
    count = 0
    for i in distance:
        if i != INF:
            max_dis = max(max_dis, i)
            count += 1
    index = distance.index(max_dis)
    print(count, max_dis)


for _ in range(int(input())):
    n, d, c = map(int, input().split())
    data = [[] for _ in range(n + 1)]

    for _ in range(d):
        a, b, s = map(int, input().split())
        data[b].append((a, s))

    dijkstra(c)
