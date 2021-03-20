point_data = list(map(float, input().split()))
n, m = map(int, input().split())
watch_data = []
alpha_data = []
for _ in range(n):
    watch_data.append(list(input()))
for _ in range(n):
    alpha_data.append(list(input()))

dont_watch = []
during_watch = []

# 안본것과 보던 것 분류.
for i in range(n):
    for j in range(m):
        if watch_data[i][j] == 'Y':
            dont_watch.append([i, j])
        elif watch_data[i][j] == 'O':
            during_watch.append([i, j])

result = []

# 안본 것 먼저 좌표 뺴고, 점수랑 정렬해서 삽입
for i in dont_watch:
    x, y = i[0], i[1]
    result.append([alpha_data[x][y], point_data[ord(alpha_data[x][y])-65], x, y])
result.sort(reverse=True, key=lambda x: x[1])

result1 = []
for i in during_watch:
    x, y = i[0], i[1]
    result1.append([alpha_data[x][y], point_data[ord(alpha_data[x][y])-65], x, y])

result1.sort(reverse=True, key=lambda x:x[1])
for i in range(len(result1)):
    result.append(result1[i])

for i in range(len(result)):
    for j in range(len(result[i])):
        print(result[i][j], end=' ')
    print()