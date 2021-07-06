result = []

def dfs(check, idx, cnt, nums, target, test):
    global count
    if cnt == test:
        calcul(check, nums, target)
        print(check)
        return

    for i in range(idx, len(check)):
        if not check[i]:
            check[i] = True
            dfs(check, i, cnt + 1, nums, target, test)
            check[i] = False



def calcul(check, nums, target):
    sum = 0
    for i in range(len(check)):
        if check[i]:
            sum += nums[i]
        else:
            sum -= nums[i]

    if sum == target:
        result.append(1)


def solution(numbers, target):
    check = [False for _ in range(len(numbers))]

    for i in range(len(check)):
        dfs(check, 0, 0, numbers, target, i)
    return (len(result))


print(solution([1, 1, 1, 1, 1], 3))
