n = int(input())


def sum_re(cnt):
    if cnt == n:
        return n
    print("Hello", cnt)
    sum_re(cnt + 1)
    print("Hi", cnt)

sum_re(0)
