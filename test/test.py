from sys import stdin

N = int(input())
nums = []
for num in map(int, stdin.readline().split()):
    nums.append(num)

ordersCheck = [False] * 8
orders = [0] * 8
curMax = 0


def recursive(index):
    global curMax
    # 탈출조건: N개의 숫자의 자리배열이 끝났다는 뜻이므로
    if index == N:
        sum = 0
        for i in range(1, N):
            sum += abs(nums[orders[i]] - nums[orders[i - 1]])
        curMax = max(sum, curMax)
        return

    for i in range(N):
        # i번째 자리가 비어있다면
        if ordersCheck[i] == False:
            # index를 i번째에 위치
            orders[index] = i
            ordersCheck[i] = True
            # 다음으로 넘긴다
            recursive(index + 1)
            # i번째 위치 사용 해제
            ordersCheck[i] = False


recursive(0)
print(curMax)
