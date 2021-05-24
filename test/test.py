x = int(input())
y=""
while x > 0:
    y = str(x % 2) + y
    x //= 2
print(y)

data = [0, 0, 0, 0]
count = 0
for i in range(len(y)-1, -1, -1):
    data[count] = int(y[i])
    count+= 1
print(data)