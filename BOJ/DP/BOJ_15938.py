x, y = map(int, input().split())
t = int(input())

xh, yh = map(int, input().split())

n = int(input())

obstacle_data = {}
for _ in range(n):
    input_x, input_y = map(int, input().split())
    obstacle_data[(input_x, input_y)] = 1

result = 0


def dfs(px, py, cnt):
    global result
    if px == xh and py == yh:
        result += 1
        return
    if cnt == t:
        return

    if not obstacle_data.get((px, py)):
        dfs(px + 1, py, cnt + 1)
        dfs(px - 1, py, cnt + 1)
        dfs(px, py + 1, cnt + 1)
        dfs(px, py - 1, cnt + 1)


dfs(x, y, 0)
print((result))
