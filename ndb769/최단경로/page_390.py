import heapq

INF = int(1e9)


def solved():
    n, m = map(int, input().split())
    data = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        data[a].append(b)
        data[b].append(a)
    distance = [INF for _ in range(n+1)]
    distance[0] = 0

    q = []
    # 힙 큐에 시작점, 거리 넣기
    heapq.heappush(q, (0, 1))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        distance[now] = dist
        for i in data[now]:
            heapq.heappush(q, (dist+1, i))

    result = max(distance)
    count = 0
    index = 0
    for i in range(1, len(distance)):
        if result == distance[i]:
            if index == 0:
                index = i
            count += 1
    print(index, result, count)
solved()



