import sys
sys.setrecursionlimit(111111)

v = int(input())
data = [[] for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]

for _ in range(v):
    com = list(map(int, sys.stdin.readline().split()))

    for i in range(1, len(com), 2):
        if com[i] == -1:
            break
        data[com[0]].append([com[i], com[i + 1]])

result2 = 0
result2_idx = 0


def dfs2(start, sum):
    global result2
    global result2_idx
    visited[start] = True
    if result2 < sum:
        result2 = sum
        result2_idx = start


    for i in data[start]:
        if not visited[i[0]]:
            dfs2(i[0], sum + i[1])


# 반복문으로 구현해보기.
def dfs(start, sum):
    global result2
    global result2_idx
    stack = []
    stack.append((start, sum))

    while stack:
        pop_node,pop_sum  = stack.pop()
        visited[pop_node] = True

        if result2 < pop_sum:
            result2 = pop_sum
            result2_idx = pop_node


        for i in data[pop_node]:
            if not visited[i[0]]:
                x, y = i
                stack.append((x, y+pop_sum))




dfs(1, 0)
visited = [False for _ in range(v + 1)]
dfs(result2_idx, 0)
print(result2)
