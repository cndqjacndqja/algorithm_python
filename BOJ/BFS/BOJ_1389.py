from _collections import deque

n, m = map(int, input().split())

data = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    data[x].append(y)
    data[y].append(x)

def bfs(idx):
    q = deque()
    q.append(idx)

    while q:


for index in range(1, n+1):
