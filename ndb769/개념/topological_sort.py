from _collections import deque

v, e = map(int, input().split())
indegree = [0 for _ in range(v + 1)]
data = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().split())
    data[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)

        for i in data[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
