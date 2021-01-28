t = int(input())

for _ in range(t):
    n = int(input())


    data = []
    for i in range(n):
        x, y = map(int, input().split())
        data.append([x, y])
    data.sort(key=lambda x:x[0])
    min = data[0][1]
    cnt = 1
    for i in range(1, n):
        if min > data[i][1]:
            min = data[i][1]
            cnt +=1

    print(cnt)
