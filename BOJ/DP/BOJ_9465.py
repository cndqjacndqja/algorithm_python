t = int(input())

for _ in range(t):
    n = int(input())
    data = []
    for _ in range(2):
        data.append(list(map(int, input().split())))

    data[0][1] += data[1][0]
    data[1][1] += data[0][0]
    for j in range(2, n):
        data[0][j] += max(data[1][j - 1], data[1][j - 2])
        data[1][j] += max(data[0][j - 1], data[0][j - 2])

    print(max(data[0][n - 1], data[1][n - 1]))
