from _collections import deque

n, m = map(int, input().split())
data = [[] for _ in range(n+1)]
distance = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    distance[b] += 1

def solved():
    q = deque()
    for i in range(1, n+1):
        if distance[i] == 0:
            q.append((i, 1))
    result = []

    while q:
        pop_node, round = q.popleft()
        result.append((pop_node, round))

        for i in data[pop_node]:
            distance[i] -= 1
            if distance[i] == 0:
                q.append((i, round+1))

    result.sort()
    for i in result:
        print(i[1], end=' ')

solved()