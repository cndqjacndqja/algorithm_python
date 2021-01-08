n = int(input())

cal = [3, 2, -1]

dp_result = [0] * (n + 1)
dp_result[1] = 0


def calculation(n):
    for i in range(2, n + 1):
        dp_result[i] = dp_result[i-1] +1
        if i % 3 == 0 and dp_result[i//3] + 1 < dp_result[i]:
            dp_result[i] = dp_result[i//3] + 1
        if i % 2 == 0 and dp_result[i//2]+1 < dp_result[i]:
            dp_result[i] = dp_result[i//2]+1

calculation(n)
print(dp_result[n])
