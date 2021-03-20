import numpy

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

result = []

black_point = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            black_point.append([i, j])


def check_bos(x, y, size):
    for i in range(size):
        for j in range(size):
            if data[x + i][y + j] == 0:
                return False
    return True


for size in range(1, n + 1):
    num_data = numpy.array(data)

    size_count = 0

    for i in range(len(black_point)):

        nx, ny = black_point[i][0], black_point[i][1]
        if check_bos(nx, ny, size):
            size_count += 1

    if size_count != 0:
        result.append([size, size_count])

total = 0
for i in result:
    total += i[1]
print("total: {0}".format(total))

for i in range(len(result)):
    print("size[{0}]: {1}".format(result[i][0], result[i][1]))
