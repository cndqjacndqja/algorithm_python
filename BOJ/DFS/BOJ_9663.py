n = int(input())


def check_up(x):
    for i in range(1, x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(x):
    global result

    if x > n:
        result += 1
    else:
        for i in range(1, n+1):
            row[x] = i
            if check_up(x):
                dfs(x + 1)


row = [0 for _ in range(16)]
result = 0
dfs(1)
print(result)
