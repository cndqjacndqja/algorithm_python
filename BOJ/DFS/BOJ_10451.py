import sys
sys.setrecursionlimit(11111)


def dfs(x):
    visited[x] = True
    number = data[x]
    if visited[number]:
        return
    dfs(number)


for _ in range(int(input())):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]

    result = 0
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
            result += 1
    print(result)
