price = 1000 - int(input())

arr = [500, 100, 50, 10, 5, 1]


index = 0
result = 0
while True:
    if index > 5:
        break

    if arr[index] <= price:
        price -= arr[index]
        result += 1
    else:
        index += 1

print(result)


a = 1000 - int(input())
b = [500, 100, 50, 10, 5, 1]
count = 0
for i in b:
    count += a // i
    a %= i
print(count)