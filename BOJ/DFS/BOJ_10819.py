from itertools import permutations

n = int(input())


def solved():
    data = list(map(int, input().split()))

    data_per = list(permutations(data, len(data)))
    result = 0
    for i in data_per:
        result = max(result, cal(i))
    dfs(0, data)
    # print(result)


def cal(data):
    sum = 0
    for i in range(len(data) - 1):
        sum += abs(data[i] - data[i + 1])
    return sum


result = [0 for _ in range(n)]
result_sum = 0
visited = [0 for _ in range(n)]


def dfs(m, data):
    global result_sum
    if m == len(data):
        sum = 0
        for i in range(len(data) - 1):
            sum += abs(result[i] - result[i+1])
        result_sum = max(result_sum, sum)
        return

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            result[m] = data[i]
            dfs(m + 1, data)
            visited[i] = 0




solved()
print(result_sum)