data = list(input())
plus = 0
minus = 0

for i in data:
    if i == '(':
        minus += 1
    elif i == ')':
        plus += 1

if plus == minus:
    print("YES")
else:
    print("NO")