from heapq import heappush, heappop

n, m = map(int, input().split())

indegree = [0 for _ in range(n + 1)]
data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    indegree[b] += 1


def topology_sort():
    q = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(q, i)

    result = []

    while q:
        node = heappop(q)
        result.append(node)

        for i in data[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heappush(q, i)

    for i in result:
        print(i, end=' ')
topology_sort()



