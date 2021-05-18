data = list(input())
s = []
sum = 0
result = 0
flag = True
for i in data:
    if i == '(':
        if len(s) == 0:
            result += sum
            sum = 0
        s.append('(')
    if i == '[':
        if len(s) == 0:
            result += sum
            sum = 0
        s.append('[')
    if i == ')':
        if s[-1] == '(':
            s.pop()
            if sum == 0:
                sum += 2
            else:
                sum *= 2
        else:
            flag = False
    if i == ']':
        if s[-1] == '[':
            s.pop()
            if sum == 0:
                sum += 3
            else:
                sum *= 3
        else:
            flag = False
    print(sum)
    print(result)
print(result)
