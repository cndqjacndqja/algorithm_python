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