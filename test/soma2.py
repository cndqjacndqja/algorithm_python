n = int(input())

data = list(map(int, input().split()))

result = [1 for _ in range(3)]
for i in range(3):
    start = i
    visited = [False for _ in range(n)]
    while True:
        move = data[start]
        start += move
        if visited[start] == False:
            result[i] += 1
            visited[start] = True

        elif visited[start]:
            result[i] += 1
            break
print(max(result))