import sys

sys.setrecursionlimit(10000000)

result = []


def fibo(n):
    if n == 1:
        return 1
    result.append(n)
    return fibo(n - 1)

print(fibo(5))
print(result)