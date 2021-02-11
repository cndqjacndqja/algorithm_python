
def dfs(x):
    visited[x] = True
    cycle.append(x)
    number = data[x]
    if visited[number]:
        if number in cycle:
            return True
    else:
        dfs(number)


for _ in range(int(input())):
    n = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n+1)]

    result = 0
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            bol = dfs(i)
            if bol:
                result += 1
    print(result)


# 왜 dfs에서 return True를 했을 떄, dfs(number)를 거친 dfs는 None을 반환하지...?
# bol = dfs(i)에서의 dfs랑 dfs(number)랑 다르게 인식하는건가,,,? 뭐지