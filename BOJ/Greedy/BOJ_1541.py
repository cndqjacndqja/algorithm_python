data = input().split("-")

plus = 0
minus = 0
for i in range(len(data)):
    if i == 0:
        first = data[i].split("+")
        for j in first:
            plus += int(j)
    else:
        minus_data = data[i].split("+")
        for j in minus_data:
            minus += int(j)

print(plus - minus)
