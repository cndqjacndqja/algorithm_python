import copy

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dp_data = copy.deepcopy(data)
for i in range(n-1):
    for j in range(len(data[i])):
        data[i+1][j] = max(data[i][j]+dp_data[i+1][j], data[i+1][j])
        data[i + 1][j+1] = max(data[i][j] + dp_data[i + 1][j+1], data[i + 1][j+1])

print(max(data[n-1]))