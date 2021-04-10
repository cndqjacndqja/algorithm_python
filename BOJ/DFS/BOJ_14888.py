n = int(input())
data = list(map(int, input().split()))
dx = list(map(int, input().split()))

result_max = -int(1e9)
result_min = int(1e9)


def dfs(cnt, param_data):
    global result_max
    global result_min
    if cnt == n:
        result_max = max(result_max, param_data)
        result_min = min(result_min, param_data)
        return
    for i in range(4):
        if dx[i] != 0:
            if i == 0:
                dx[i] -= 1
                dfs(cnt + 1, param_data + data[cnt])
            if i == 1:
                dx[i] -= 1
                dfs(cnt + 1, param_data - data[cnt])
            if i == 2:
                dx[i] -= 1
                dfs(cnt + 1, param_data * data[cnt])
            if i == 3:
                dx[i] -= 1
                dfs(cnt + 1, int(param_data / data[cnt]))
            dx[i] += 1


dfs(1, data[0])
print(result_max)
print(result_min)
