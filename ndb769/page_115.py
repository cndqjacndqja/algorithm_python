start = input()
dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [-2, -1, 1, 2, 2, 1, -1, -2]

x = ord(start[0]) - 97
y = int(start[1]) - 1
cnt = 0

for i in range(8):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        cnt += 1

print(cnt)
