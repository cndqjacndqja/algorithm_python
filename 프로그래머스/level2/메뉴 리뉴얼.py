result_level = []
result = []
max_num = 0


def dfs(cnt, check, idx, count, orders):
    if cnt == count:
        calcul(check, orders)
        return
    for i in range(idx, len(check)):
        if not check[i]:
            check[i] = True
            dfs(cnt + 1, check, i, count, orders)
            check[i] = False


def calcul(check, orders):
    global max_num
    test_str = ""
    count = 0
    for i in range(len(check)):
        if check[i]:
            test_str += chr(65 + i)

    for o in orders:
        flag = True
        for i in test_str:
            if not i in o:
                flag = False

        if flag:
            count += 1

    if count == max_num:
        result_level.append(test_str)
    elif count > max_num:
        max_num = count
        result_level.clear()
        result_level.append(test_str)


def solution(orders, course):
    global max_num

    for i in course:
        check = [False for _ in range(26)]
        max_num = 2
        dfs(0, check, 0, i, orders)
        for i in result_level:
            result.append(i)
        result_level.clear()
    result.sort()
    return result


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4])
