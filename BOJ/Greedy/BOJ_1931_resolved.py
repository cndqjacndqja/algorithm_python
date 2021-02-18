n = int(input())

data = []
for _ in range(n):
    x, y = map(int, input().split())
    data.append([x, y])

data.sort(key=lambda x: (x[1], x[0]))
result = 1
standard = data[0][1]
for i in range(1, n):
    if standard <= data[i][0]:
        result +=1
        standard = data[i][1]

print(result)