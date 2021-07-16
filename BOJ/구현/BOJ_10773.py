n = int(input())
s = []
for _ in range(n):
    data = int(input())
    if data == 0 and len(s) > 0:
        s.pop()
    else:
        s.append(data)

print(sum(s))