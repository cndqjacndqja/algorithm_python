n = int(input())

# 상, 하, 좌, 우, ㅇ대각위, 대각
dx, dy = [-1, 1, 0, 0, -1, 1, -1, 1], [0, 0, -1, 1, -1, -1, 1, 1]
data = [[0 for _ in range(n)] for _ in range(n)]

