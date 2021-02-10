n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

cnt = 0
sum = 0
while True:
    if cnt == m:
        break
    for i in range(k):
        if cnt != m:
            sum += data[0]
            cnt +=1
    if cnt != m:
        sum += data[1]
        cnt += 1

print(sum)