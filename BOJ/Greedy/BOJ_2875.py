n, m, k = map(int, input().split())

result = 0
while True:
    if n - 2 >= 0 and m - 1 >= 0:
        if n - 2 + m - 1 >= k:
            n -= 2
            m -= 1
            result += 1
        else:
            break
    else:
        break
print(result)
