import heapq

INF = int(1e9)

n, m, C = map(int, input().split())

data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((b, c))


def dijkstra():
    q = []
    distance = [INF for _ in range(n + 1)]
    distance[C] = 0
    heapq.heappush(q, (C, 0))

    while q:
        node, dis = heapq.heappop(q)

        if distance[node] < dis:
            continue

        for i in data[node]:
            if dis + i[1] < distance[i[0]]:
                distance[i[0]] = dis + i[1]
                heapq.heappush(q, (i[0], i[1] + dis))

    count = 0
    max_value = 0
    for i in distance:
        if i != INF:
            count += 1
            max_value = max(max_value, i)

    if count != 0:
        print(count - 1, max_value)
    else:
        print(-1)


dijkstra()
