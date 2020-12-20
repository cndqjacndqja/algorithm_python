import sys


a, b, c = map(int, sys.stdin.readline().rstrip().split(" "))


def lmc(x, y):
    return x * y // gcd(x, y)


def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


a = lmc(a, b)
a = lmc(a, c)

print(a)
