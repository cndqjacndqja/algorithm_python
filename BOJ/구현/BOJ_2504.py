data = list(input())
s = []
b = []
cof = 1
isPaired = True
ans = 0

for i in range(len(data)):
    if data[i] == '(':
        s.append(i)
        cof *= 2
    elif data[i] == '[':
        b.append(i)
        cof *= 3
    elif data[i] == ')':
        if s:
            if data[i - 1] == '(':
                ans += cof
            s.pop()
            cof //= 2
        else:
            isPaired = False
            break
    elif data[i] == ']':
        if b:
            if data[i - 1] == '[':
                ans += cof
            b.pop()
            cof //= 3
        else:
            isPaired = False
            break

if not b and not s and isPaired:
    print(ans)
else:
    print(0)
