n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

matrix2 = [[0] * 3 for _ in range(n)]

for i in range(n):
    if i == 0:
        matrix2[i] = matrix[0]
    else:
        matrix2[i][0] = min(matrix2[i-1][1], matrix2[i-1][2]) + matrix[i][0]
        matrix2[i][1] = min(matrix2[i-1][0], matrix2[i-1][2]) + matrix[i][1]
        matrix2[i][2] = min(matrix2[i-1][0], matrix2[i-1][1]) + matrix[i][2]

print(min(min(matrix2[n-1][0], matrix2[n-1][1]), matrix2[n-1][2]))