import sys

n, m, k = map(int, sys.stdin.readline().split(" "))

a = list(map(int, sys.stdin.readline().split(" ")))

a.sort()
a.reverse()

num1 = a[0]
num2 = a[1]
print(num1, num2)
result = 0

while m != 0:
    for i in range(k):
        m -= 1
        result += num1
        if m == 0:
            break
    if m == 0:
        break
    else:
        result += num2
        m -= 1

print(result)
