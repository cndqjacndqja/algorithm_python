n, k = map(int, input().split())

data = []
for _ in range(n):
    data.append(int(input()))

result = 0
index = len(data) - 1
while True:
    if index < 0:
        break
    if data[index] <= k:
        k -= data[index]
        result += 1
    else:
        index -= 1

print(result)