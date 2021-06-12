from _collections import deque

n, m = map(int, input().split())
level = [0 for _ in range(n+1)]
data = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    level[b] += 1

def solved():
    q = deque()
    for i in range(1, n+1):
        if level[i] == 0:
            q.append(i)

    while q:
        pop_node = q.popleft()
        print(pop_node, end=' ')

        for i in data[pop_node]:

            level[i] -= 1
            if level[i] == 0:
                q.append(i)
solved()
