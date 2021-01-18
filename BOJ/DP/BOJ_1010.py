t = int(input())


def counting(n, i):
    sum = 1
    if i == 0:
        return 1
    for j in range(i):
        sum *= n - j
    d = 1
    for z in range(i, 0, -1):
        d *= z
    return sum // d


for _ in range(t):
    n, m = map(int, input().split())
    print(counting(m,n))