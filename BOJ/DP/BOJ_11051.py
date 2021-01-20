n, k = map(int, input().split())


def combi(n, k):
    sum = 1
    devide = 1
    for i in range(k):
        sum *= (n - i)
    for i in range(1, k + 1):
        devide *= i
    return (sum // devide) % 10007


print(combi(n, k))
