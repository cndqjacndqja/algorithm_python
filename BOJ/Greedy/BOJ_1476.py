E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
result = 1
while True:
    if e == E and s == S and m == M:
        print(result)
        break
    if e == 15:
        e = 1
    else:
        e += 1
    if s == 28:
        s = 1
    else:
        s += 1

    if m == 19:
        m = 1
    else:
        m += 1
    result += 1





