from heapq import heappush, heappop

n, m, r = map(int, input().split())
item_value = [0] + list(map(int, input().split()))
data = [[] for _ in range(n + 1)]
INF = int(1e9)
for _ in range(r):
    a, b, c = map(int, input().split())
    data[a].append((b, c))
    data[b].append((a, c))

def dijkstra(start):
    q = []
    distance = [INF for _ in range(n+1)]
    heappush(q, (0, start))
    sum_data = item_value[start]
    distance[start] = 0
    visited = [False for _ in range(n+1)]
    visited[start] = True

    while q:
        dis, node = heappop(q)

        for i in data[node]:
            cost = dis + i[1]
            if cost < distance[i[0]] and cost <= m:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
                sum_data += item_value[i[0]]


    return sum_data

def solved():
    result = []
    for i in range(1, n+1):
        result.append(dijkstra(i))
    print(max(result))

solved()



