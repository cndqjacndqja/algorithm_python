n = int(input())
# data = []
# dp = [0 for _ in range(n)]
# for _ in range(n):
#     data.append(list(map(int, input().split())))


# def solve(i):
#     if i > n - 1:
#         return 0
#     ret = 0
#     if i + data[i][0] <= n:
#         ret = solve(i + data[i][0]) + data[i][1]
#     ret = max(ret, solve(i + 1))
#     return ret



def facto(i):
    if i > n:
        return 1
    return i * facto(i+1)

print(facto(1))