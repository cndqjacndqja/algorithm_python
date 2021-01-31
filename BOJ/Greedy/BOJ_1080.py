n, m = map(int, input().split())

A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]


def change(x, y, data):
    for i in range(3):
        for j in range(3):
            if data[x + i][y + j] == 0:
                data[x + i][y + j] = 1
            elif data[x + i][y + j] == 1:
                data[x + i][y + j] = 0


def check(A, B):
    for i in range(n):
        for j in range(m):
            if A[i][j] != B[i][j]:
                return False
    return True


count = 0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j] != B[i][j]:
            change(i, j, A)
            count += 1
if check(A, B):
    print(count)
else:
    print(-1)