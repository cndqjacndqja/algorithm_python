# while문으로 구현

from _collections import deque

n, m = map(int, input().split())
data = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

def dfs(start):
    visited = [False for _ in range(n+1)]
    stack = [start]

    while stack:
        node = stack.pop()
        for i in data[node]:
            if not visited[i]:
                stack.append(i)
                visited[i] = True
                print(i)

dfs(1)

# 왜 pop을 하고 나서 방문체크를 할까?
# 이 코드를 해석하자.
# stack리스트에 첫 시작 점을 넣은 후, 그것이 빌 때까지 while문을 반복한다.
# stack