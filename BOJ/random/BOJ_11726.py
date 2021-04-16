
def factory(x):
    j = 1
    for i in range(1,x+1):
        j *= i
    return j
if __name__ == "__main__":
    n = int(input())

    count = 0
    i = 0
    while i <= n:
        for j in range(0, n+1):
            if i + j is n:
                test = i //2
                count += factory(test+j)//(factory(test)*factory(j))
                break
        i += 2

    print(count%10007)
