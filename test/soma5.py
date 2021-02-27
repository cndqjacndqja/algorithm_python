from _collections import deque

string = input().split()
data = [[] for _ in range(26)]

for i in range(int(input())):
    x, y = map(ord, input().split())
    x -= 97
    y -= 97
    data[x].append(y)
    data[y].append(x)

def dfs(start):
    visited = list()
    q = deque()

    q.append(start)
    while q:
        pop_data = q.pop()
        if pop_data not in visited:
            visited.append(pop_data)
            for i in data[pop_data]:
                if i not in visited:
                    q.append(data[pop_data])
                    print(pop_data, end=' ')

for i in range(26):
    if len(data[i]) == 1:
        dfs(i)


