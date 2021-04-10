n = int(input())
data = list(map(int, input().split()))
dx = list(map(int, input().split()))

result = []


def dfs(cnt, param_data):
    if cnt == n:
        result.append(param_data)
        return

    if dx[0] > 0:
        dx[0] -= 1
        dfs(cnt + 1, param_data + data[cnt])
        dx[0] += 1
    if dx[1] > 0:
        dx[1] -= 1
        dfs(cnt + 1, param_data - data[cnt])
        dx[1] += 1
    if dx[2] > 0:
        dx[2] -= 1
        dfs(cnt + 1, param_data * data[cnt])
        dx[2] += 1
    if dx[3] > 0:
        dx[3] -= 1
        dfs(cnt + 1, int(param_data / data[cnt]))
        dx[3] += 1


dfs(1, data[0])
print(max(result))
print(min(result))
