from heapq import heappush, heappop

v, e = map(int, input().split())
k = int(input())
data = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    data[a].append((b, c))

INF = int(1e9)
distance = [INF for _ in range(v + 1)]


def dijkstra():
    q = [(0, k)]
    distance[k] = 0

    while q:
        dis, node = heappop(q)

        # 이것의 의미는 무엇인가? 힙에서 팝한 데이터의 dis가 무엇을 의미하지?
        # 현재 노드에서 갈 수 있는 간선의 길이를 팝한건가? 근데 이미 이전에 거기 방문했던 거리보다
        # 더 길다면 그냥 스킵하겠다는 의미구나!
        if dis > distance[node]:
            continue

        for i in data[node]:
            pop_node, pop_dis = i
            now_ids = dis + pop_dis
            if now_ids < distance[pop_node]:
                distance[pop_node] = now_ids
                heappush(q, (now_ids, pop_node))
    for i in range(1, v+1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print("INF")


dijkstra()
