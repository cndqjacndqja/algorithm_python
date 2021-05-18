data = []
for _ in range(9):
    data.append(int(input()))

visited_check = [False for _ in range(9)]


def dfs(visited, cnt, x):
    if cnt == 7:
        solution(visited)
        return

    for i in range(x, 9):
        if not visited[i]:
            visited[i] = True
            dfs(visited, cnt + 1, i)
            visited[i] = False


def solution(visited):
    result = []
    for i in range(9):
        if visited[i]:
            result.append(data[i])
    if sum(result) == 100:
        result.sort()
        for i in result:
            print(i)
        exit()


dfs(visited_check, 0, 0)
