a = int(input())
b = int(input())
c = int(input())

data = str(a*b*c)
data = list(data)

result = [0] * 10

for i in data:
    result[int(i)] += 1

for i in result:
    print(i)
