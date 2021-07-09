def dfs(check, cnt, idx, numbers):
    if cnt == 2:
        calcul(check, numbers)
        return

    for i in range(idx, len(check)):
        if not check[i]:
            check[i] = True
            dfs(check, cnt + 1, i, numbers)
            check[i] = False


result = []


def calcul(check, numbers):
    data = 0
    for i in range(len(check)):
        if check[i]:
            data += numbers[i]
    result.append(data)


def solution(numbers):
    check = [False for _ in range(len(numbers))]

    dfs(check, 0, 0, numbers)

    result_data = []
    for i in set(result):
        result_data.append(i)
    result_data.sort()
    return result_data

print(solution([2,1,3,4,1]))
