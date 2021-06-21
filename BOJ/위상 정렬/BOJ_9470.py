from _collections import deque

for T in range(int(input())):
    k, m, p = map(int, input().split())

    data = [[] for _ in range(m + 1)]
    distance = [0 for _ in range(m + 1)]
    level_count = [0 for _ in range(m + 1)]
    for _ in range(p):
        a, b = map(int, input().split())
        data[a].append(b)
        distance[b] += 1

    q = deque()
    for i in range(1, m + 1):
        if distance[i] == 0:
            q.append(i)
            level_count[i] = 1
    result = 0
    while q:
        pop_node = q.popleft()
        result = pop_node

        for i in data[pop_node]:
            distance[i] -= 1
            if distance[i] == 0:
                q.append(i)

            if level_count[i] == 0:
                level_count[i] = level_count[pop_node]
            else:
                if level_count[i] == level_count[pop_node]:
                    level_count[i] += 1
                else:
                    level_count[i] = level_count[pop_node]

    print(T+1, level_count[result])
