n = int(input())
x, y = map(int, input().split())
m = int(input())
data = [[] for _ in range(n + 1)]

# 양쪽에 연결하는 이유는?? 그럼 다른 문제들에서는 양쪽에 연결하면 안되나??
for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

visited = [False for _ in range(n + 1)]

result = 0


def dfs(param_x, cnt):
    global result
    if param_x == y:
        result = cnt
        return

    for i in data[param_x]:
        if not visited[i]:  # 만약 방문처리를 안하면 어떻게 될까?, 외워서 하지 말자. 하나하나에 다 이유가 있다.
            visited[i] = True
            dfs(i, cnt + 1)


dfs(x, 0)
if result == 0:
    print(-1)
else:
    print(result)
