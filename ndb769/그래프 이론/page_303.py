from _collections import deque
import copy

n = int(input())
data = [[] for _ in range(n + 1)]
time = [0 for _ in range(n + 1)]
indegree = [0 for _ in range(n+1)]


def solved():
    for i in range(1, n+1):
        com = list(map(int, input().split()))
        time[i] = com[0]
        for x in com[1:-1]:
            indegree[i] += 1
            data[x].append(i)

    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in data[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    print(result)

solved()




