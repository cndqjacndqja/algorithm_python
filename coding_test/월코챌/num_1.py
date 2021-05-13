import math

def solution(left, right):
    result = 0
    for i in range(left, right+1):
        if get_division(i):
            result += i
        else:
            result -= i

    return result


def get_division(n):
    count = 0
    for i in range(1, n+ 1):
        if n % i == 0:
            count +=1

    if count % 2 == 0:
        return True
    else:
        return False

