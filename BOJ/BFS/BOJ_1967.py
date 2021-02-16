n = int(input())
data = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    insert_n, insert_v, insert_d = map(int, input().split())
    data[insert_n].append([insert_v, insert_d])
    data[insert_v].append([insert_n, insert_d])

result = 0
result_idx = 0
def dfs(start):
    global result
    global result_idx
    stack = []
    stack.append((start, 0))

    while stack:
        pop_n, pop_d = stack.pop()
        visited[pop_n] = True

        if result < pop_d:
            result = pop_d
            result_idx = pop_n

        for i in data[pop_n]:
            if not visited[i[0]]:
                stack.append((i[0], i[1]+pop_d))

dfs(1)
visited = [False for _ in range(n + 1)]
dfs(result_idx)
print(result)