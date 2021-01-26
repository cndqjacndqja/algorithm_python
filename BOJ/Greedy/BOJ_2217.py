n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)
result = 0
for i in range(len(data)):
    if result < data[i] * (i+1):
        result = data[i] * (i+1)

print(result)

