data = list(input())
data.sort(reverse=True)
sum = 0
for i in data:
    sum += int(i)
if sum % 3 != 0 or '0' not in data:
    print(-1)
else:
    print(''.join(data))

