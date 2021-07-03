result = 0

# 소수인지 판별하는 함수.
def judge_sosu(a):
    for i in range(2, a//2+1):
        if a % i == 0:
            return False
    return True

def calcul_num(check, num):
    data = 0
    for i in range(len(check)):
        if check[i]:
            data+=num[i]
    return data



# 모든 경우의 수 dfs로 구현하기.
def dfs(check, idx, cnt, nums):
    global result
    if cnt == 3:
        data = calcul_num(check, nums)
        if judge_sosu(data):
            result+=1
        return

    for i in range(idx, len(check)):
        if not check[i]:
            check[i] = True
            dfs(check, i+1, cnt+1, nums)
            check[i] = False

def solution(nums):
    check = [False for _ in range(len(nums))]
    dfs(check, 0, 0, nums)
    return result

