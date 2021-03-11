n = int(input())
data = list(map(int, input().split()))

plus, minus, multi, divi = map(int, input().split())

result = []


def dfs(start, num):
    global plus, minus, multi, divi
    if start == n:
        result.append(num)

    if plus > 0:
        plus -= 1
        dfs(start + 1, num + data[start])
        plus += 1
    if minus > 0:
        minus -= 1
        dfs(start + 1, num - data[start])
        minus += 1
    if multi > 0:
        multi -= 1
        dfs(start + 1, num * data[start])
        multi += 1
    if divi > 0:
        divi -= 1
        dfs(start + 1, int(num / data[start]))
        divi += 1

dfs(1, data[0])
print(max(result))
print(min(result))
