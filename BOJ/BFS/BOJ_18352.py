from _collections import deque

n, m, k, x = map(int, input().split())
data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)


def bfs(start):
    q = deque()
    q.append(start)
    visited = [-1 for _ in range(n+1)]
    visited[start] += 1
    result = []

    while q:
        pop_data = q.popleft()
        if visited[pop_data] == k:
            result.append(pop_data)
        if visited[pop_data] < k:
            for i in data[pop_data]:
                if visited[i] == -1:
                    q.append(i)
                    visited[i] = visited[pop_data] + 1
    return result


def solved():
    result = bfs(x)
    result.sort()
    if len(result) == 0:
        print(-1)
    else:
        for i in result:
            print(i)
solved()