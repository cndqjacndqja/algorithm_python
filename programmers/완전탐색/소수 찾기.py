from itertools import permutations


def solution(numbers):
    data = list(numbers)
    result = []
    for i in range(1, len(numbers) + 1):
        per_data = list(map(''.join, permutations(data, i)))
        for i in per_data:
            if sosu(int(i), result):
                result.append(int(i))
    return len(result)

def sosu(num, result):
    if num == 0 or num == 1 or num in result:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True