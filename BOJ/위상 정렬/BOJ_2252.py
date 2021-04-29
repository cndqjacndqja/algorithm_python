from _collections import deque

n, m = map(int, input().split())
data = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    indegree[b] += 1


def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)

        for i in data[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')


topology_sort()

