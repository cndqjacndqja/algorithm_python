n, l, r = map(int, input().split())

data = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for _ in range(n):
    data.append(list(map(int, input().split())))

result_cnt = 0


def solve():
    global result_cnt

    while True:
        team = []
        print(data)
        for i in range(n):
            for j in range(n):
                for z in range(4):
                    nx, ny = i + dx[z], j + dy[z]
                    if 0 <= nx < n and 0 <= ny < n:
                        if l <= abs(data[i][j] - data[nx][ny]) <= r:
                            if (i, j) not in team:
                                team.append((i, j))
                            if (nx, ny) not in team:
                                team.append((nx, ny))

        if len(team) == 0:
            return
        print(team)
        result_cnt += 1
        sum = 0
        for i in team:
            x, y = i
            sum += data[x][y]
        print(sum)
        sum = sum // len(team)
        print(sum, len(team))
        for i in team:
            x, y = i
            data[x][y] = sum
        team.clear()


solve()
print(result_cnt)
