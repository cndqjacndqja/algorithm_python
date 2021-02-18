import bisect

n = int(input())

data =[]
for _ in range(n):
    data.append(int(input()))

up_data = []
down_data = []
zero = False

for i in range(n):
    if data[i] > 0:
        up_data.append(data[i])
    elif data[i] < 0:
        down_data.append(data[i])
    elif data[i] == 0:
        zero = True

up_data.sort(reverse=True)
for i in range(1, len(up_data), 2):
    if up_data[i] == 1:
        up_data[i] += up_data[i - 1]
        up_data[i - 1] = 0
    else:
        up_data[i] *= up_data[i-1]
        up_data[i-1] = 0

down_data.sort()
for i in range(1, len(down_data), 2):
    down_data[i] *= down_data[i-1]
    down_data[i-1] = 0
if len(down_data) > 0:
    if down_data[len(down_data)-1] < 0:
        if zero:
            down_data[len(down_data)-1] = 0

print(sum(up_data)+sum(down_data))
