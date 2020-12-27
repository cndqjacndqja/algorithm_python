from _collections import deque

n, m = map(int, input().split(" "))
MAX = 100001
visited = [0] * MAX


def bfs(xn, xm):
    q = deque()
    q.append(xn)

    while q:
        v = q.popleft()
        if v == xm:
            return visited[v]

        for i in (v - 1, v + 1, v * 2):
            if 0 <= i < MAX and visited[i] == 0:
                visited[i] += visited[v] + 1
                q.append(i)


print(bfs(n, m))

