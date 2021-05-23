n = int(input())
check = [False for _ in range(n)]
orders = [0 for _ in range(n)]
data = list(map(int, input().split()))
result = []



def dfs(idx):
    if idx == n - 1:
        result.append(cal_solution())
        return

    for i in range(n):
        if not check[i]:
            orders[idx] = i
            check[i] = True
            dfs(idx + 1)
            check[i] = False


def cal_solution():
    sum = 0
    for i in range(n - 1):
        sum += abs(data[orders[i]] - data[orders[i + 1]])
    return sum


dfs(0)
print(max(result))
