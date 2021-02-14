a, p = map(int, input().split())
data = []
data.append(a)
while True:
    pop_data = str(data[-1])
    sum = 0
    for i in range(len(pop_data)):
        plus = int(pop_data[i])
        sum += plus**p

    if sum in data:
        index = data.index(sum)
        print(index)
        break
    data.append(sum)

