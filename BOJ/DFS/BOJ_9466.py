import sys
sys.setrecursionlimit(111111)


def dfs(x):
    global result
    visited[x] = True
    cycle.append(x)
    number = data[x]
    if visited[number]:
        if number in cycle:
            index = cycle.index(number)
            result += cycle[index: ]
        return
    else:
        dfs(number)


for _ in range(int(input())):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    result = []
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-len(result))