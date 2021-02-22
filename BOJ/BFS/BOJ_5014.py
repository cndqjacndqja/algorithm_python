from _collections import deque

F, S, G, U, D = map(int, input().split())

dx = [U, -D]
visited = [-1 for _ in range(F + 1)]


def solve():
    q = deque()
    q.append((S, 0))
    visited[S] = 0
    while q:
        pop_idx, pop_cnt = q.popleft()

        for i in dx:
            nx = pop_idx + i
            if 1 <= nx <= F and visited[nx] == -1:
                q.append((nx, pop_cnt+1))
                visited[nx] = pop_cnt+1

    if visited[G] == -1:
        print("use the stairs")
    else:
        print(visited[G])

solve()
