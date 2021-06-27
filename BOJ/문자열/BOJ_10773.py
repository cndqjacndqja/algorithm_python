n = int(input())
data = []
for _ in range(n):
    a = int(input())
    if a == 0:
        data.pop()
    else:
        data.append(a)

print(sum(data))