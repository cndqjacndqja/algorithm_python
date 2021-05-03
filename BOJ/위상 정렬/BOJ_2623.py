from _collections import deque

n, m = map(int, input().split())
data = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
flag = True
for _ in range(m):
    pd_data = list(map(int, input().split()))
    for i in range(1, len(pd_data) - 1):
        data[pd_data[i]].append(pd_data[i + 1])
        indegree[pd_data[i + 1]] += 1

result = []


def topology_sort():
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        result.append(node)

        for i in data[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)


topology_sort()
if len(result) != n:
    print(0)
else:
    for i in result:
        print(i)
